# 1.3.0.84: new pickups (grenade box, ammo box, kit, coin, medal), city specialties, gas cylinders, hydrant, hanging sign, harbor container
from playwright.sync_api import sync_playwright
SP='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/ui/'
U='file:///mnt/user-data/outputs/soto_slug_tex_edition.html'
START="(a)=>{PROG.tut=true; selChar=a[0]; ST.char=a[0]; ST.stage=a[1]; ST.startPart=a[2]||1; MAP={from:null,to:a[1],t:0,fire:false}; mapStart(); setGod(false); ST.lives=99; for(let i=0;i<200;i++) update(); PL.chute=false; PL.air=false; PL.jy=0; ST.wavePlan=[]; ST.dogPlan=[]; ST.ev=null; enemies=[]; return scn.map(o=>o.k).join(' ');}"
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':800}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U); pg.wait_for_timeout(1500); print('version',pg.evaluate("VERSION"))
    for st,pt,nm in [(2,1,'Genova 1'),(2,2,'Genova 2'),(1,1,'Lione'),(4,1,'Mantova'),(3,1,'Marsiglia 1'),(3,2,'Marsiglia 2')]:
        print(nm,pg.evaluate(START,[0,st,pt]))
    pg.evaluate(START,[0,2,1])
    print('item art',pg.evaluate("()=>['bombs','sgammo','kit','coin','medal'].map(k=>k+':'+(ITEM_SPR[k]&&ITEM_SPR[k].width)).join(' ')"))
    print('pickups',pg.evaluate("""()=>{ const out={}; PL.hp=5; for(const k of ['kit','coin','medal']){ items=[]; const s0=ST.score; dropItem(PL.x,GROUND-10,k); for(let i=0;i<60;i++) update(); out[k]=ST.score-s0; } out.hp=PL.hp; return out; }"""))
    print('specialty',pg.evaluate("""()=>{ items=[]; dropItem(PL.x+200,GROUND-10,true); const it=items[0]; return [it.kind,it.si,specName(it.si)]; }"""))
    r=pg.evaluate("""()=>{ civs=[]; obs=[]; const g=scn.find(o=>o.k==='gas'); g.x=ST.scrollX+330; PL.x=ST.scrollX+60; spawnEnemy(); const e=enemies[enemies.length-1]; e.x=g.x-e.w/2+30; const st=[];
      for(let i=0;i<3;i++) scnHit(g,1,g.x,GROUND-40); for(let i=0;i<120;i++){ update(); if(!st.includes(g.st)) st.push(g.st); } return {st,enemyDead:e.hp<=0}; }""")
    print('gas',r)
    r=pg.evaluate("""()=>{ const h=scn.find(o=>o.k==='hyd'); h.x=ST.scrollX+300; spawnEnemy(); const e=enemies[enemies.length-1]; e.x=h.x-e.w/2+10; const x0=e.x; const st=[];
      for(let i=0;i<2;i++) scnHit(h,1,h.x,GROUND-20); for(let i=0;i<60;i++){ update(); if(!st.includes(h.st)) st.push(h.st); } return {st,pushed:Math.round(e.x-x0)}; }""")
    print('hydrant',r)
    r='signs set aside in 1.3.0.85' if not pg.evaluate("()=>scn.some(o=>o.k==='sign')") else pg.evaluate("""()=>{ enemies=[]; const s=scn.find(o=>o.k==='sign'); s.x=ST.scrollX+300; spawnEnemy(); const e=enemies[enemies.length-1]; e.x=s.x-e.w/2; const hb=scnBox(s); const st=[];
      shots.push({x:s.x,y:hb.y+hb.h/2,vx:0,vy:0,life:5,dmg:1,k:'b',pl:true}); for(let i=0;i<2;i++) scnHit(s,1,s.x,hb.y+10); for(let i=0;i<90;i++){ update(); if(!st.includes(s.st)) st.push(s.st); } return {st,enemyHit:e.hp<=0||e.flash>0}; }""")
    print('sign',r)
    r=pg.evaluate("""()=>{ enemies=[]; const c=scn.find(o=>o.k==='cont'); c.x=ST.scrollX+330; PL.x=ST.scrollX+40; spawnEnemy(); const e=enemies[enemies.length-1]; e.x=c.x-e.w/2; const st=[];
      PL.x=c.x-200; for(let i=0;i<200;i++){ update(); if(!st.includes(c.st)) st.push(c.st); } return {st,enemyDead:e.hp<=0}; }""")
    print('container',r)
    oy=pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'; return document.getElementById('cv').getBoundingClientRect().top}")
    for st,pt,nm in [(2,1,'genova'),(3,1,'mars')]:
        pg.evaluate(START,[0,st,pt])
        pg.evaluate("""()=>{ civs=[]; obs=[]; traffic=[]; const sx=ST.scrollX, pick=k=>scn.find(o=>o.k===k); const put=(k,x)=>{const o=pick(k); if(o) o.x=sx+x; };
          put('cont',300); put('gas',420); put('hyd',40); PL.x=sx+180; PL.dir=1; items=[]; dropItem(sx+250,GROUND,'bombs'); dropItem(sx+330,GROUND,true); for(const it of items){it.y=GROUND;it.land=true;} render(); }""")
        pg.screenshot(path=SP+f'obj84_{nm}.png',clip={'x':0,'y':oy+40,'width':480,'height':580})
    print('ERR',errs); b.close()
