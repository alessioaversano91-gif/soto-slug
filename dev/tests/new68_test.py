# 1.3.0.68: Genova vehicles = white/green car, van, Carabinieri; no old burnt-car cover in Genova
from playwright.sync_api import sync_playwright
SP='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/ui/'
U='file:///mnt/user-data/outputs/soto_slug_tex_edition.html'
START="(a)=>{PROG.tut=true; selChar=a[0]; ST.char=a[0]; ST.stage=a[1]; ST.startPart=a[2]||1; MAP={from:null,to:a[1],t:0,fire:false}; mapStart(); setGod(true); for(let i=0;i<200;i++) update(); PL.chute=false; PL.air=false; PL.jy=0; ST.wavePlan=[]; ST.dogPlan=[]; ST.ev=null; enemies=[]; return 1;}"
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':800}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U); pg.wait_for_timeout(1300)
    mix={}
    for i in range(12):
        pg.evaluate(START,[0,2,1+i%3]); r=pg.evaluate("()=>[civs.map(c=>c.col).join(''),obs.filter(o=>o.type==='car').length]")
        for ch in r[0]: mix[ch]=mix.get(ch,0)+1
        assert r[1]==0, 'old car cover still in Genova'
        assert r[0].count('c')<=1
    print('types over 12 levels',mix)
    pg.evaluate(START,[0,4,1]); print('Mantova old cover kept',pg.evaluate("()=>obs.filter(o=>o.type==='car').length>=0"))
    # every vehicle through every state, recording missing frames
    for col in 'wgvc':
        pg.evaluate(START,[0,2,1])
        r=pg.evaluate("""(col)=>{ const miss=new Set(); const df=drawFrame;
          const c=civs[0]; c.col=col; c.hp=c.max=CIV_HPS[col]; ST.scrollX=c.x-260; PL.x=ST.scrollX+100;
          const chk=()=>{ const k=civFrame(c); if(!S[k]||!CVM[k]) miss.add(k); };
          const seen=[]; PL.shootCd=0; doShoot(); for(let i=0;i<300&&c.st!=='gone';i++){ update(); chk(); if(seen[seen.length-1]!==c.st) seen.push(c.st); if(i%20===0) render(); }
          const d=civs[1]||civs[0]; d.col=col; d.hp=d.max=CIV_HPS[col]; d.st='alarm'; d.calm=999; ST.scrollX=d.x-260; PL.x=ST.scrollX+100;
          for(let i=0;i<400&&d.st!=='wreck';i++){ if(d.st==='alarm'){ civHit(d,1,d.x+50,GROUND-60); } update(); const k=civFrame(d); if(!S[k]) miss.add(k); if(seen[seen.length-1]!==d.st) seen.push(d.st); }
          render(); return {states:seen.join('>'),missing:[...miss]}; }""",col)
        print(col,r); pg.screenshot(path=f'{SP}veh_{col}.png',clip={'x':0,'y':300,'width':480,'height':300})
    # line-up for a picture
    pg.evaluate(START,[0,2,2])
    pg.evaluate("()=>{ civs=['g','v','c'].map((col,i)=>({col,x:ST.scrollX+60+i*330,st:i===1?'alarm':'park',hp:CIV_HPS[col],max:CIV_HPS[col],t:0,stT:0,calm:999,flash:0,vx:0})); ST.scrollX+=0; PL.x=ST.scrollX+30; render(); }")
    pg.screenshot(path=SP+'veh_line.png',clip={'x':0,'y':300,'width':480,'height':300})
    print('ERR',errs); b.close()
