# 1.3.0.80: LIFE default, Genova 1-2 final barrage, boss tuning (Lione, Mantova), Marseille part 1 shorter
from playwright.sync_api import sync_playwright
U='file:///mnt/user-data/outputs/soto_slug_tex_edition.html'
START="(a)=>{PROG.tut=true; selChar=0; ST.char=0; ST.stage=a[0]; ST.startPart=a[1]||1; MAP={from:null,to:a[0],t:0,fire:false}; mapStart(); for(let i=0;i<200;i++) update(); PL.chute=false; PL.air=false; PL.jy=0; ST.wavePlan=[]; ST.dogPlan=[]; ST.ev=null; enemies=[]; return ST.maxScroll;}"
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':800}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U); pg.wait_for_timeout(1300); print('version',pg.evaluate("VERSION"))
    print('LIFE default',pg.evaluate("()=>ST.god===false&&document.getElementById('godBtn').textContent"))
    pg.evaluate("()=>setGod(true)")
    for lv in (1,2):
        pg.evaluate(START,[2,lv])
        r=pg.evaluate("""()=>{ ST.scrollX=ST.maxScroll-1; PL.x=ST.scrollX+200; let wave=false,flashes=[],win=false,boss=false;
          for(let i=0;i<4000;i++){ update(); const f=document.getElementById('flash').textContent; if(!flashes.includes(f)) flashes.push(f); if(ST.wave&&ST.wave.final) wave=true; if(enemies.some(e=>e.type===5)) boss=true;
            for(const e of enemies) if(e.type!==5&&e.t>40) e.hp=0;   // the player clears the barrage
            if(ST.mode==='win'){win=true;break;} } return {wave,boss,win,flashes:flashes.filter(Boolean)}; }""")
        print('Genova level',lv,r)
    pg.evaluate(START,[2,3]); print('Genova 3 still has the tank',pg.evaluate("()=>{ ST.scrollX=ST.maxScroll-1; PL.x=ST.scrollX+200; for(let i=0;i<300;i++) update(); return enemies.some(e=>e.type===5); }"))
    for st in (1,4,3):
        pg.evaluate(START,[st,1]); print('boss',st,pg.evaluate("()=>{ spawnBoss(); const e=enemies.find(e=>e.type===5); return {hp:e.max,wait:e.waitBase,p2:e.V.p2.join(',')}; }"))
    print('Marseille lengths',pg.evaluate(START,[3,1]),pg.evaluate(START,[3,2]),'Mantova',pg.evaluate(START,[4,1]))
    print('ERR',errs); b.close()
