# 1.3.0.65: city events, elite bottles, shot power-ups, tank weak spot, objectives/stars
from playwright.sync_api import sync_playwright
SP='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/ui/'
U='file:///mnt/user-data/outputs/soto_slug_tex_edition.html'
START="(a)=>{PROG.tut=true; selChar=a[0]; ST.char=a[0]; ST.stage=a[1]; MAP={from:null,to:a[1],t:0,fire:false}; mapStart(); setGod(true); for(let i=0;i<200;i++) update(); PL.chute=false; PL.air=false; PL.jy=0; ST.wavePlan=[]; ST.carPlan=[]; ST.dogPlan=[]; ST.trevPlan=[]; enemies=[]; return 1;}"
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':800}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U); pg.wait_for_timeout(1200)
    # --- events: force each kind, run, render, screenshot
    for st,k in [(1,'fog'),(4,'night'),(3,'wind'),(2,'bottles')]:
        pg.evaluate(START,[0,st])
        r=pg.evaluate("(k)=>{ ST.ev={k,at:0,t:0,on:false,done:false,amt:0,dir:1}; const x0=PL.x; let falls0=0; for(let i=0;i<300;i++){ update(); if(falls.length>falls0) falls0=falls.length; } render(); return {on:ST.ev.on,amt:+ST.ev.amt.toFixed(2),wind:+ST.wind.toFixed(2),dx:Math.round(PL.x-x0),falls:falls0,dropT:ST.dropT}; }",k)
        pg.screenshot(path=f'{SP}ev_{k}.png',clip={'x':0,'y':0,'width':480,'height':640}); print('event',k,r)
        r=pg.evaluate("()=>{ ST.ev.t=EV_DUR; for(let i=0;i<120;i++) update(); return [ST.ev.done,ST.wind,ST.ev.amt]; }"); print('  end',r)
    # --- elites
    pg.evaluate(START,[0,4])
    r=pg.evaluate("""()=>{ const R=Math.random; const out={};
      for(const k of ['armor','kami','split']){ enemies=[]; Math.random=()=>0; spawnEnemy(); Math.random=R; const e=enemies[0]; e.elite=null; e.hp=e.max=3;
        e.elite=k; if(k==='armor'){e.hp=e.max=6;} if(k==='split'){e.hp=e.max=4;} if(k==='kami'){e.keep=0;e.shootT=9999;}
        e.x=PL.x+150; out[k]={hp:e.hp}; }
      // armor: one bullet
      enemies=[]; spawnEnemy(); let e=enemies[0]; e.elite='armor'; e.hp=e.max=8; e.x=PL.x+60; shots.push({k:'bul',x:e.x-5,y:e.y+e.h/2,vx:9,vy:0,dmg:1,life:60}); updateShots(); out.armorAfter1=+e.hp.toFixed(2);
      // kami: walks in and explodes, hurting a nearby bottle
      enemies=[]; spawnEnemy(); spawnEnemy(); e=enemies[0]; e.elite='kami'; e.keep=0; e.x=PL.x+160; const o=enemies[1]; o.x=PL.x+120; o.hp=o.max=3; ST.dmgTaken=0;
      for(let i=0;i<160&&!e.boomed;i++) update(); out.kami={boomed:!!e.boomed,neighbourDead:o.hp<=0,dmgTaken:ST.dmgTaken};
      // split: kill it -> two minis
      enemies=[]; spawnEnemy(); e=enemies[0]; e.elite='split'; e.x=PL.x+200; e.hp=1; e.hp=0; killEnemy(e); out.split=enemies.filter(x=>x.mini).length;
      render(); out.eliteK=ST.eliteK; return out; }""")
    print('elites',r)
    pg.evaluate("()=>{ enemies=[]; for(const k of ['armor','kami','split']){ spawnEnemy(); const e=enemies[enemies.length-1]; e.elite=k; e.x=PL.x+90+enemies.length*90; e.keep=999; e.vx=0; } spawnEnemy(); const e=enemies[enemies.length-1]; e.x=PL.x+60; e.elite='split'; e.hp=0; killEnemy(e); render(); }")
    pg.screenshot(path=SP+'elites.png',clip={'x':0,'y':0,'width':480,'height':640})
    # --- power-ups (Albi gun)
    r=pg.evaluate("""()=>{ const out={}; enemies=[]; items=[];
      for(const k of ['ptri','ppierce','pboom']){ dropItem(PL.x,GROUND-40,k); const it=items[items.length-1]; it.y=GROUND; it.land=true; it.x=PL.x; updateItems(); out[k]=ST.mod&&ST.mod.k;
        shots=[]; PL.shootCd=0; PL.melee=0; doShoot(); out[k+'_shots']=shots.filter(s=>s.k==='bul').length; out[k+'_flags']=shots.map(s=>(s.pk?'P':'')+(s.xb?'X':'')).join(','); }
      // pierce through two enemies
      ST.mod={k:'pierce',t:600}; enemies=[]; spawnEnemy(); spawnEnemy(); enemies[0].x=PL.x+60; enemies[1].x=PL.x+130; enemies.forEach(e=>{e.hp=e.max=9;e.keep=999;});
      shots=[]; PL.shootCd=0; doShoot(); for(let i=0;i<30;i++) updateShots(); out.pierceHits=enemies.filter(e=>e.hp<9).length;
      ST.mod={k:'boom',t:600}; enemies=[]; spawnEnemy(); spawnEnemy(); enemies[0].x=PL.x+80; enemies[1].x=PL.x+100; enemies.forEach(e=>{e.hp=e.max=9;e.keep=999;});
      shots=[]; PL.shootCd=0; doShoot(); for(let i=0;i<30;i++) updateShots(); out.boomHits=enemies.filter(e=>e.hp<9).length;
      ST.mod={k:'tri',t:2}; for(let i=0;i<3;i++) update(); out.expired=ST.mod===null; return out; }""")
    print('powerups',r)
    # Pinuccia axe with triple
    pg.evaluate(START,[4,2])
    r=pg.evaluate("()=>{ ST.mod={k:'tri',t:600}; shots=[]; PL.shootCd=0; doShoot(); for(let i=0;i<12;i++) update(); return shots.filter(s=>s.k==='axe').length; }"); print('axe tri',r)
    # --- tank weak spot
    pg.evaluate(START,[0,1])
    r=pg.evaluate("""()=>{ ST.scrollX=ST.maxScroll; PL.x=ST.scrollX+260; for(let i=0;i<400;i++) update(); const t=enemies.find(e=>e.type===5); if(!t) return 'no tank';
      t.weakCd=1; for(let i=0;i<3;i++) update(); const h0=t.hp; t.hp-=5; update(); const d1=h0-t.hp;
      let k=0; while(!t.stagger&&k<40){ t.hp-=4; update(); k++; } const stag=t.stagger;
      render(); return {weakT:t.weakT>0||stag>0, doubled:d1, stagger:stag}; }""")
    print('tank weak',r); pg.screenshot(path=SP+'weak.png',clip={'x':0,'y':0,'width':480,'height':640})
    # --- objectives: specialties, evaluation, stars, map and win screen
    pg.evaluate(START,[0,2])
    r=pg.evaluate("""()=>{ const out={n:ST.specs.length,ys:ST.specs.map(s=>GROUND-s.y)};
      for(const s of ST.specs){ ST.scrollX=s.x-200; PL.x=s.x; PL.jy=-60; PL.vy=0; PL.air=true; updateVariety(); } out.got=ST.spec.got.length; PL.jy=0; PL.air=false;
      ST.bombsUsed=0; ST.bossTime=42; PROG.stars={}; out.eval=evalObjectives(); out.stars=PROG.stars[2]; return out; }""")
    print('objectives',r)
    pg.evaluate("()=>{ ST.scrollX=ST.maxScroll; ST.bossTime=50; doWin(); }"); pg.wait_for_timeout(400)
    print('win rows',pg.evaluate("()=>[...document.querySelectorAll('#winstats .obj')].map(d=>d.textContent.trim())"))
    pg.screenshot(path=SP+'win65.png')
    pg.evaluate("()=>{ showMap(2,1); MAP.t=999; render(); }"); pg.wait_for_timeout(200); pg.screenshot(path=SP+'map65.png',clip={'x':0,'y':0,'width':480,'height':640})
    pg.evaluate("()=>{ refreshStageRecords(); }"); print('records',pg.evaluate("()=>document.getElementById('lr1').innerHTML.length>50"))
    print('ERR',errs); b.close()
