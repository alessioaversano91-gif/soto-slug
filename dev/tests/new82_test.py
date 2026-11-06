# 1.3.0.82: level objects — explosive barrel, mystery crate, market stall, hostage (one set per city)
from playwright.sync_api import sync_playwright
SP='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/ui/'
U='file:///mnt/user-data/outputs/soto_slug_tex_edition.html'
START="(a)=>{PROG.tut=true; selChar=a[0]; ST.char=a[0]; ST.stage=a[1]; ST.startPart=a[2]||1; MAP={from:null,to:a[1],t:0,fire:false}; mapStart(); setGod(true); for(let i=0;i<200;i++) update(); PL.chute=false; PL.air=false; PL.jy=0; ST.wavePlan=[]; ST.dogPlan=[]; ST.ev=null; enemies=[]; return scn.map(o=>o.k+':'+o.city).join(' ');}"
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':800}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U); pg.wait_for_timeout(1500); print('version',pg.evaluate("VERSION"))
    for st,pt,nm in [(2,1,'Genova 1'),(2,3,'Genova 3'),(1,1,'Lione'),(4,1,'Mantova'),(3,1,'Marsiglia 1'),(3,2,'Marsiglia 2')]:
        print(nm,pg.evaluate(START,[0,st,pt]))
    print('overlaps',pg.evaluate("""()=>{ let bad=0; for(const o of scn){ for(const c of civs) if(o.x>c.x-30&&o.x<c.x+civW(c)+30) bad++; for(const ob of obs) if(o.x>ob.x-20&&o.x<ob.x+ob.w+20) bad++; } return bad; }"""))
    pg.evaluate(START,[0,1,1])
    r=pg.evaluate("""()=>{ civs=[]; obs=[]; const B=scn.find(o=>o.k==='barrel'); B.x=ST.scrollX+300; PL.x=ST.scrollX+60; const s0=ST.score;
      spawnEnemy(); const e=enemies[enemies.length-1]; e.x=B.x-e.w/2+20; const st=[];
      for(let i=0;i<3;i++) scnHit(B,1,B.x,GROUND-40); for(let i=0;i<60;i++){ update(); if(!st.includes(B.st)) st.push(B.st); }
      return {states:st,enemyDead:e.hp<=0, score:ST.score-s0}; }""")
    print('barrel',r)
    r=pg.evaluate("""()=>{ const C=scn.find(o=>o.k==='crate'); C.x=ST.scrollX+300; const n=items.length, ne=enemies.length, s0=ST.score; for(let i=0;i<4;i++) scnHit(C,1,C.x,GROUND-30); for(let i=0;i<40;i++) update(); return {st:C.st, reward: items.length>n?'item':enemies.length>ne?'bottle':ST.score>s0?'points':'none'}; }""")
    print('crate',r)
    r=pg.evaluate("""()=>{ const S2=scn.find(o=>o.k==='stall'); S2.x=ST.scrollX+300; for(let i=0;i<10;i++) scnHit(S2,1,S2.x,GROUND-60); for(let i=0;i<60;i++) update(); return {st:S2.st, goods:goods.length}; }""")
    print('stall',r)
    r=pg.evaluate("""()=>{ const H=scn.find(o=>o.k==='host'); H.x=ST.scrollX+250; PL.x=ST.scrollX+120; const n=items.length; const st=[]; scnHit(H,1,H.x,GROUND-40); for(let i=0;i<220;i++){ update(); if(H&&!st.includes(H.st)) st.push(H.st); } return {states:st, item:items.length>n, freed:ST.hostN, gone:!scn.includes(H)}; }""")
    print('hostage',r)
    # screenshot with one of each in view
    oy=pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'; return document.getElementById('cv').getBoundingClientRect().top}")
    for st,nm in [(2,'genova'),(1,'lione'),(3,'mars'),(4,'mantova')]:
        pg.evaluate(START,[0,st,1])
        pg.evaluate("""()=>{ civs=[]; obs=[]; traffic=[]; const sx=ST.scrollX; const pick=k=>scn.find(o=>o.k===k);
          const st=pick('stall'), h=pick('host'), b1=pick('barrel'), c1=pick('crate'); if(st) st.x=sx+330; if(h) h.x=sx+200; if(b1) b1.x=sx+40; if(c1) c1.x=sx+445; PL.x=sx+120; PL.dir=1; render(); }""")
        pg.screenshot(path=SP+f'obj82_{nm}.png',clip={'x':0,'y':oy+180,'width':480,'height':440})
    print('ERR',errs); b.close()
