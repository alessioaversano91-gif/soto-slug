# 1.3.0.81: civil cars without alarm/escape (damage -> fire -> boom -> wreck), melee can't hurt them, thinner fog,
# gendarmerie never parks on a parked car, Genova end-of-level bonus, boot screen removed after loading
from playwright.sync_api import sync_playwright
SP='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/ui/'
U='file:///mnt/user-data/outputs/soto_slug_tex_edition.html'
START="(a)=>{PROG.tut=true; selChar=a[0]; ST.char=a[0]; ST.stage=a[1]; ST.startPart=a[2]||1; MAP={from:null,to:a[1],t:0,fire:false}; mapStart(); setGod(true); for(let i=0;i<200;i++) update(); PL.chute=false; PL.air=false; PL.jy=0; ST.wavePlan=[]; ST.dogPlan=[]; ST.ev=null; enemies=[]; return civs.length;}"
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':800}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U); pg.wait_for_timeout(1500); print('version',pg.evaluate("VERSION"),'boot gone',pg.evaluate("()=>!document.getElementById('boot')"))
    pg.evaluate(START,[0,2,1])
    r=pg.evaluate("""()=>{ const c=civs[0]; c.x=ST.scrollX+250; const seq=[]; const frames=[]; const sounds=[]; const o=window.sfx; 
      for(let i=0;i<20;i++){ civHit(c,1,c.x+50,GROUND-40); for(let j=0;j<6;j++) update(); if(!seq.includes(c.st)) seq.push(c.st); const f=civFrame(c).split('_')[1]; if(!frames.includes(f)) frames.push(f); }
      for(let i=0;i<200;i++){ update(); if(!seq.includes(c.st)) seq.push(c.st); const f=civFrame(c).split('_')[1]; if(!frames.includes(f)) frames.push(f); }
      return {seq,frames,x:c.x>ST.scrollX+200}; }""")
    print('car lifecycle',r)
    pg.evaluate(START,[1,2,1])
    print('melee no damage',pg.evaluate("""()=>{ const c=civs[0]; c.x=PL.x+10; const hp=c.hp; PL.dir=1; PL.meleeKind='punch'; for(let k=0;k<10;k++) meleeImpact(); return c.hp===hp; }"""))
    pg.evaluate(START,[0,1,1])
    print('gendarmerie avoids parked cars',pg.evaluate("""()=>{ let bad=0; for(let k=0;k<30;k++){ cars=[]; const c=civs[k%civs.length]; ST.scrollX=Math.max(0,c.x-300); PL.x=c.x-150; spawnCar(-1); const car=cars[0]; for(const v of civs){ if(car.stopX>v.x-100&&car.stopX<v.x+civW(v)+100) bad++; } } cars=[]; return bad; }"""))
    pg.evaluate(START,[0,2,1])
    print('Genova bonus',pg.evaluate("""()=>{ const s0=ST.score; ST.wave=null; ST.finalW=true; levelEnd(); return ST.score-s0; }"""))
    print('ERR',errs); b.close()
