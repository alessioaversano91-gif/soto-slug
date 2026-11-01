# 1.3.0.70: traffic lane at the bottom, Genova 1-2 end without boss, France SUV in Lione and Marsiglia
from playwright.sync_api import sync_playwright
SP='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/ui/'
U='file:///mnt/user-data/outputs/soto_slug_tex_edition.html'
START="(a)=>{PROG.tut=true; selChar=a[0]; ST.char=a[0]; ST.stage=a[1]; ST.startPart=a[2]||1; MAP={from:null,to:a[1],t:0,fire:false}; mapStart(); setGod(true); for(let i=0;i<200;i++) update(); PL.chute=false; PL.air=false; PL.jy=0; ST.wavePlan=[]; ST.dogPlan=[]; ST.ev=null; enemies=[]; return {civ:civs.map(c=>c.col).join(''),car:obs.filter(o=>o.type==='car').length};}"
END="""()=>{ ST.scrollX=ST.maxScroll-1; PL.x=ST.scrollX+200; let boss=false,win=false,flash=''; for(let i=0;i<400;i++){ update(); if(enemies.some(e=>e.type===5)) boss=true; if(ST.mode==='win'){win=true;break;} if(!flash) flash=document.getElementById('flash').textContent; }
  return {boss,win,part:ST.part,next:document.getElementById('nextBtn').textContent,flash}; }"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':800}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U); pg.wait_for_timeout(1300)
    print('version',pg.evaluate("VERSION"))
    for st,nm in [(1,'Lione'),(3,'Marsiglia'),(3,'Marsiglia p2'),(2,'Genova'),(4,'Mantova')]:
        r=pg.evaluate(START,[0,st,2 if 'p2' in nm else 1]); print(nm,r)
    for lv in (1,2,3):
        pg.evaluate(START,[0,2,lv]); r=pg.evaluate(END); print('Genova level',lv,r)
    pg.evaluate(START,[0,1,1]); r=pg.evaluate(END); print('Lione end',r)
    pg.evaluate(START,[0,1,1])
    # France: SUV gets hit, alarm, explodes; traffic uses the SUV at the bottom lane
    r=pg.evaluate("""()=>{ const c=civs[0]; c.x=ST.scrollX+250; PL.x=ST.scrollX+60; PL.dir=1; const st=[]; for(let i=0;i<40;i++){ civHit(c,1,c.x+50,GROUND-40); for(let j=0;j<4;j++) update(); if(!st.includes(c.st)) st.push(c.st); } 
      ST.trafT=1; const cols=new Set(); for(let i=0;i<2500;i++){ update(); traffic.forEach(v=>cols.add(v.col)); } return {states:st,traffic:[...cols]}; }""")
    print('suv',r)
    pg.evaluate(START,[0,1,1])
    pg.evaluate("()=>{ traffic=[{col:'f',dir:-1,v:-4,x:ST.scrollX+260,t:0},{col:'f',dir:1,v:4,x:ST.scrollX-20,t:0}]; civs[0].x=ST.scrollX+170; civs[0].st='alarm'; PL.x=ST.scrollX+70; render(); }")
    pg.screenshot(path=SP+'lione70.png',clip={'x':0,'y':300,'width':480,'height':500})
    pg.evaluate(START,[0,2,1])
    pg.evaluate("()=>{ traffic=[{col:'v',dir:-1,v:-4,x:ST.scrollX+260,t:0},{col:'c',dir:1,v:4,x:ST.scrollX-20,t:0}]; civs[0].x=ST.scrollX+170; PL.x=ST.scrollX+70; render(); }")
    pg.screenshot(path=SP+'genova70.png',clip={'x':0,'y':300,'width':480,'height':500})
    print('ERR',errs); b.close()
