# 1.3.0.78: Marseille bus in traffic, taxi cameo + scooter in the traffic lane + wheelie stunt at street level (twice per level, mocks you, can't be hit)
from playwright.sync_api import sync_playwright
SP='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/ui/'
U='file:///mnt/user-data/outputs/soto_slug_tex_edition.html'
START="(a)=>{PROG.tut=true; selChar=a[0]; ST.char=a[0]; ST.stage=a[1]; ST.startPart=a[2]||1; MAP={from:null,to:a[1],t:0,fire:false}; mapStart(); setGod(true); for(let i=0;i<200;i++) update(); PL.chute=false; PL.air=false; PL.jy=0; ST.wavePlan=[]; ST.dogPlan=[]; ST.ev=null; enemies=[]; return {plan:ST.stuntPlan.length};}"
RUN="""()=>{ const cols={}; let stunts='', said=0, hpMin=PL.hp, prev=null; for(let i=0;i<12000;i++){ if(ST.trafT>60) ST.trafT=60; ST.scrollX=Math.min(ST.maxScroll-10,ST.scrollX+2); PL.x=ST.scrollX+150; enemies=[]; update(); for(const v of traffic) cols[v.col]=1; if(stunt&&stunt!==prev){ stunts+=stunt.k; prev=stunt; } if(stunt&&stunt.said&&stunt.say===79) said++; if(ST.bossIn||ST.partT) break; } return {traffic:Object.keys(cols).sort().join(''),stunts,said}; }"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':800}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U); pg.wait_for_timeout(1300); print('version',pg.evaluate("VERSION"))
    for st,pt,nm in [(3,1,'Marsiglia 1'),(3,2,'Marsiglia 2'),(1,1,'Lione'),(2,1,'Genova')]:
        print(nm,pg.evaluate(START,[0,st,pt]),pg.evaluate(RUN))
    pg.evaluate(START,[0,3,1])
    r=pg.evaluate("""()=>{ ST.stuntPlan=[{at:0,k:'x'}]; for(let i=0;i<3;i++) updateStunt(); stunt.x=PL.x-20; civs=[]; obs=[]; enemies=[]; cars=[]; shots=[]; PL.shootCd=0; PL.dir=stunt.dir<0?1:-1; const hp=PL.hp; doShoot(); const sh=shots[0]; for(let i=0;i<6;i++){ updateShots(); updateStunt(); } return {bulletAlive:shots.includes(sh),hpSame:PL.hp===hp}; }""")
    print('not hittable',r)
    oy=pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'; return document.getElementById('cv').getBoundingClientRect().top}")
    pg.evaluate("()=>{ stunt={k:'x',dir:1,x:ST.scrollX+150,v:0,t:20,say:0,said:true,txt:''}; traffic=[{col:'m',dir:-1,v:-3,x:ST.scrollX+200,t:5}]; PL.x=ST.scrollX+100; render(); }")
    pg.screenshot(path=SP+'taxi78.png',clip={'x':0,'y':oy+250,'width':480,'height':390})
    print('ERR',errs); b.close()
