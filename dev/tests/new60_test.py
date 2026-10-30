from playwright.sync_api import sync_playwright
SP='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/ui/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':800}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(1200)
    # Lione: gendarme ducks under standing shots, crouched shots still hit
    r=pg.evaluate("""()=>{ PROG.tut=true; selChar=0; ST.char=0; ST.stage=1; MAP={from:null,to:1,t:0,fire:false}; mapStart(); setGod(true);
      for(let i=0;i<200;i++) update(); PL.chute=false; PL.air=false; PL.jy=0; ST.wavePlan=[]; ST.carPlan=[]; enemies=[]; spawnGendAt(PL.x+220); const e=enemies[enemies.length-1];
      e.st='walk'; e.taunted=true; e.dcd=0; e.hp=e.max=999; const R=Math.random; Math.random=()=>.01; PL.dir=1; PL.crouch=false;
      shots.push({k:'bul',x:PL.x+40,y:GROUND-80,vx:9,vy:0,dmg:1,life:60,low:false}); let st=[]; for(let i=0;i<14&&e.st!=='duck';i++){ update(); st.push(e.st); } const k0=gendKey(e);
      Math.random=R; const hp0=e.hp; shots.push({k:'bul',x:e.x-30,y:GROUND-80,vx:9,vy:0,dmg:1,life:60,low:false}); for(let i=0;i<6;i++) update(); const overHit=hp0-e.hp;
      shots.push({k:'bul',x:e.x-30,y:GROUND-40,vx:9,vy:0,dmg:1,life:60,low:true}); for(let i=0;i<6;i++) update(); const lowHit=hp0-overHit-e.hp;
      const key=gendKey(e); for(let i=0;i<40;i++) update(); return {st:st.slice(-2),k0,key,overHit,lowHit,after:e.st}; }""")
    print('duck',r)
    # tank: flash then recoil frame
    r=pg.evaluate("""()=>{ const t={type:5,hitT:9,st:'move',t:0}; const seq=[]; while(t.hitT>0){ seq.push(tankFrame(t)); t.hitT--; } return seq.join(' '); }""")
    print('tank',r)
    # Genova first screen without the lettered band
    pg.evaluate("()=>{ ST.stage=2; MAP={from:null,to:2,t:0,fire:false}; mapStart(); }"); pg.wait_for_timeout(5500); pg.screenshot(path=SP+'gen60.png',clip={'x':0,'y':0,'width':480,'height':560})
    print('ERR',errs); b.close()
