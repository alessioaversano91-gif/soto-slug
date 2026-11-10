# 1.3.0.98: enemies from above with the existing sprites — bombing run, dive, paratrooper, flock; air-kill bonus; hostages + air kills in the summary
import sys,os
from playwright.sync_api import sync_playwright
SP='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/ui/'
START=open('new86_test.py').read().split('START="')[1].split('"\n')[0]
ok=True
def chk(name,cond,info=''):
    global ok; ok&=bool(cond); print(('OK  ' if cond else 'FAIL'),name,info)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':800}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(1500); print('version',pg.evaluate("VERSION"))
    pg.evaluate(START,[0,2]); pg.evaluate("()=>{ window.__u=update; }")
    oy=pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'; return document.getElementById('cv').getBoundingClientRect().top}")
    FLY="const s=S.bottle_s; enemies.length=0; eshots.length=0; ST.amarks=[]; spawnT=99999; ST.flockT=99999; PL.hp=PL.maxHp||PL.hp; PL.inv=0; setGod(false);"
    # 1 bombing run: the flyer comes over the player, a ring appears, a cork falls and hurts if you stay
    r=pg.evaluate("()=>{"+FLY+""" enemies.push({type:2,key:'bottle_s',x:PL.x+150,y:GROUND-230,w:s.w,h:s.h,hp:3,max:3,dir:-1,vx:0,t:0,shootT:99999,flash:0,keep:150,hoverY:GROUND-230,dropT:80});
      let mark=false,cork=false,minDx=999; const hp0=PL.hp; for(let i=0;i<260;i++){ update(); const e=enemies[0]; if(e) minDx=Math.min(minDx,Math.abs(e.x+e.w/2-PL.x)); if((ST.amarks||[]).length) mark=true; if(eshots.some(b=>b.k==='cork')) cork=true; }
      return {mark,cork,minDx:Math.round(minDx),lost:hp0-PL.hp}; }""")
    chk('bombing run',r['mark'] and r['cork'] and r['minDx']<46 and r['lost']>=2,r)
    # ...and stepping aside avoids it
    r=pg.evaluate("()=>{"+FLY+""" enemies.push({type:2,key:'bottle_s',x:PL.x+150,y:GROUND-230,w:s.w,h:s.h,hp:3,max:3,dir:-1,vx:0,t:0,shootT:99999,flash:0,keep:150,hoverY:GROUND-230,dropT:80});
      const hp0=PL.hp; let dropped=false; for(let i=0;i<300;i++){ if(eshots.some(b=>b.k==='cork')) dropped=true; K.r=dropped?1:0; update(); if(dropped&&enemies[0]) enemies[0].dropT=9999; } K.r=0; return {dropped,lost:hp0-PL.hp}; }""")
    chk('cork dodged by moving',r['dropped'] and r['lost']==0,r)
    # 2 dive: at its last hit the flyer marks the spot, dives and crashes; standing there hurts, it dies without score
    r=pg.evaluate("()=>{"+FLY+""" enemies.push({type:2,key:'bottle_s',x:PL.x+120,y:GROUND-230,w:s.w,h:s.h,hp:1,max:2,dir:-1,vx:0,t:0,shootT:99999,flash:0,keep:150,hoverY:GROUND-230,dropT:9999});
      const hp0=PL.hp, sc0=ST.score; let mark=false,dive=false; for(let i=0;i<140;i++){ update(); if((ST.amarks||[]).length) mark=true; if(enemies[0]&&enemies[0].dive) dive=true; }
      return {mark,dive,left:enemies.length,lost:hp0-PL.hp,score:ST.score-sc0}; }""")
    chk('dive hits who stays',r['mark'] and r['dive'] and r['left']==0 and r['lost']>=2 and r['score']==0,r)
    r=pg.evaluate("()=>{"+FLY+""" enemies.push({type:2,key:'bottle_s',x:PL.x+120,y:GROUND-230,w:s.w,h:s.h,hp:1,max:2,dir:-1,vx:0,t:0,shootT:99999,flash:0,keep:150,hoverY:GROUND-230,dropT:9999});
      const hp0=PL.hp; K.l=1; for(let i=0;i<140;i++) update(); K.l=0; return {left:enemies.length,lost:hp0-PL.hp}; }""")
    chk('dive dodged by moving',r['left']==0 and r['lost']==0,r)
    # 3 paratrooper: comes down, lands, becomes a walker that shoots; shot in the air = bonus and air kill, no corpse
    r=pg.evaluate("()=>{"+FLY+""" spawnPara(); const e=enemies[0]; const y0=e.y; let shotsInAir=0, landed=-1; for(let i=0;i<700&&landed<0;i++){ update(); if(e.para&&eshots.length) shotsInAir++; if(!e.para) landed=i; }
      for(let i=0;i<40;i++) update(); return {y0:Math.round(y0),landed,onGround:Math.abs(e.y-(GROUND-e.h))<1,shotsInAir,type:e.type,moves:e.shootT<9000}; }""")
    chk('paratrooper lands and walks',r['landed']>100 and r['onGround'] and r['shotsInAir']==0 and r['moves'],r)
    pg.evaluate("()=>{"+FLY+" spawnPara(); const e=enemies[0]; e.x=PL.x+60; e.y=GROUND-330; }"); pg.evaluate("()=>{ window.update=()=>{}; render(); }")
    pg.screenshot(path=SP+'air98_para.png',clip={'x':0,'y':oy+60,'width':480,'height':440}); pg.evaluate("()=>{ window.update=window.__u; }")
    r=pg.evaluate("""()=>{ ST.airK=0; const a0=PROG.air||0, sc0=ST.score, c0=corpses.length; const e=enemies[0]; e.type=0; e.key='bottle'; PL.dir=1; const ex=e.x; let aimed=false;
      K.s=1; for(let i=0;i<120&&e.hp>0;i++){ e.x=ex; update(); if(PL.aimUpT>0) aimed=true; } K.s=0; return {dead:e.hp<=0,aimed,airK:ST.airK,air:(PROG.air||0)-a0,score:ST.score-sc0,corpses:corpses.length-c0}; }""")
    chk('paratrooper shot in the air',r['dead'] and r['aimed'] and r['airK']==1 and r['air']==1 and r['score']>=900 and r['corpses']==0,r)
    # melee can't reach it in the air (Seba bare-handed)
    # 4 flock: three flyers cross, three rings, three corks; they leave the screen
    r=pg.evaluate("()=>{"+FLY+""" setGod(true); spawnFlock(); const n=enemies.length; let marks=0,corks=0,seenM=new Set(),seenC=new Set(); for(let i=0;i<420;i++){ update(); for(const m of ST.amarks||[]) seenM.add(m); for(const c of eshots) if(c.k==='cork') seenC.add(c); }
      return {n,marks:seenM.size,corks:seenC.size,left:enemies.filter(e=>e.fly).length}; }""")
    chk('flock',r['n']==3 and r['marks']==3 and r['corks']==3 and r['left']==0,r)
    pg.evaluate("()=>{"+FLY+" setGod(true); spawnFlock(); for(let i=0;i<70;i++) update(); window.update=()=>{}; render(); }")
    pg.screenshot(path=SP+'air98_flock.png',clip={'x':0,'y':oy+60,'width':480,'height':440}); pg.evaluate("()=>{ window.update=window.__u; }")
    # flock timer: fires on its own in a normal level, never in the tutorial / boss rush / during the boss
    r=pg.evaluate("()=>{"+FLY+""" setGod(true); ST.flockT=3; ST.tut=null; for(let i=0;i<6;i++) update(); const a=enemies.filter(e=>e.fly).length; enemies.length=0; ST.flockT=3; ST.bossIn=true; for(let i=0;i<6;i++) update(); const b=enemies.filter(e=>e.fly).length; ST.bossIn=false; return [a,b]; }""")
    chk('flock timer',r==[3,0],r)
    # 5 summary rows
    r=pg.evaluate("()=>{ ST.hostN=1; ST.hostTot=2; ST.airK=4; const s0=ST.score; stageSummary(); const t=document.getElementById('winstats').textContent; return [t.includes('OSTAGGI LIBERATI')&&t.includes('1/2'), t.includes('ABBATTUTI IN VOLO'), t]; }")
    chk('summary rows',r[0] and r[1],r[2][:160])
    r=pg.evaluate("()=>{ ST.hostN=2; ST.hostTot=2; ST.airK=0; stageSummary(); const t=document.getElementById('winstats').textContent; return [t.includes('TUTTI LIBERI'), !t.includes('IN VOLO')]; }")
    chk('summary all freed / no air row',r==[True,True],r)
    chk('medal listed',pg.evaluate("()=>MEDALS.some(m=>m[0]==='air')"))
    chk('no page errors',not errs,errs)
    b.close()
print('PASS' if ok else 'FAIL')
