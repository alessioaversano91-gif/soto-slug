# 1.3.0.67: civilian car 1 in the Genova levels - alarm, peel-out to the right, fire and explosion, wreck
from playwright.sync_api import sync_playwright
SP='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/ui/'
U='file:///mnt/user-data/outputs/soto_slug_tex_edition.html'
START="(a)=>{PROG.tut=true; selChar=a[0]; ST.char=a[0]; ST.stage=a[1]; ST.startPart=a[2]||1; MAP={from:null,to:a[1],t:0,fire:false}; mapStart(); setGod(true); for(let i=0;i<200;i++) update(); PL.chute=false; PL.air=false; PL.jy=0; ST.wavePlan=[]; ST.dogPlan=[]; ST.ev=null; enemies=[]; return civs.map(c=>[c.col,Math.round(c.x/ST.maxScroll*100)]);}"
SETUP="()=>{ const c=civs[0]; ST.scrollX=c.x-260; PL.x=ST.scrollX+120; PL.dir=1; enemies=[]; return c.st; }"
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':800}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U); pg.wait_for_timeout(1300)
    for lvl in (1,2,3): print('genova',lvl,'cars',pg.evaluate(START,[0,2,lvl]))
    print('lione cars',pg.evaluate(START,[0,1,1]))
    # few shots -> alarm -> peel out to the right
    pg.evaluate(START,[0,2,1]); pg.evaluate(SETUP)
    r=pg.evaluate("""()=>{ const c=civs[0], seen=[]; const x0=c.x;
      for(let i=0;i<3;i++){ PL.shootCd=0; doShoot(); for(let k=0;k<8;k++){ update(); } }
      for(let i=0;i<260&&civs.includes(c);i++){ update(); if(seen[seen.length-1]!==c.st) seen.push(c.st); if(i===40) render(); }
      return {states:seen.join('>'),hp:c.hp,moved:Math.round(c.x-x0),gone:!civs.includes(c)}; }""")
    print('few shots',r)
    # keep shooting -> burn -> boom -> wreck, nearby bottle dies, score +1000
    pg.evaluate(START,[0,2,1]); pg.evaluate(SETUP)
    r=pg.evaluate("""()=>{ const c=civs[0]; spawnEnemy(); const e=enemies[enemies.length-1]; e.x=c.x+civW(c)/2; e.keep=999; e.hp=e.max=6; const s0=ST.score; const seen=[];
      for(let i=0;i<400&&c.st!=='wreck';i++){ PL.shootCd=0; if(c.st==='alarm'||c.st==='park') doShoot(); update(); if(seen[seen.length-1]!==c.st) seen.push(c.st); if(c.st==='boom'&&c.stT===4) render(); }
      return {states:seen.join('>'),enemyDead:e.hp<=0,score:ST.score-s0,booms:ST.civBoomN||0}; }""")
    print('many shots',r); pg.screenshot(path=SP+'civ_boom.png',clip={'x':0,'y':0,'width':480,'height':640})
    # screenshots: parked, alarm, peel
    pg.evaluate(START,[0,2,2]); pg.evaluate(SETUP)
    pg.evaluate("()=>{ render(); }"); pg.screenshot(path=SP+'civ_park.png',clip={'x':0,'y':0,'width':480,'height':640})
    pg.evaluate("()=>{ PL.shootCd=0; doShoot(); for(let k=0;k<20;k++) update(); render(); }"); pg.screenshot(path=SP+'civ_alarm.png',clip={'x':0,'y':0,'width':480,'height':640})
    pg.evaluate("()=>{ for(let k=0;k<75;k++) update(); render(); }"); pg.screenshot(path=SP+'civ_peel.png',clip={'x':0,'y':0,'width':480,'height':640})
    # bomb next to a car
    pg.evaluate(START,[2,2,3]); pg.evaluate(SETUP)
    r=pg.evaluate("()=>{ const c=civs[0]; explodeShot({x:c.x+40,y:GROUND-30,dmg:15},60); for(let i=0;i<200;i++) update(); return c.st; }"); print('bomb',r)
    # Pinuccia's axe does not get lost on a car
    pg.evaluate(START,[4,2,1]); pg.evaluate(SETUP)
    r=pg.evaluate("()=>{ const c=civs[0]; PL.shootCd=0; doShoot(); let back=false; for(let i=0;i<200;i++){ update(); } return [c.hp<CIV_HP, !shots.some(s=>s.k==='axe')]; }"); print('axe',r)
    print('ERR',errs); b.close()
