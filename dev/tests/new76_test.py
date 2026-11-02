# 1.3.0.76: Fiat 500 in the Genova and Lione traffic only (never parked, not in Marsiglia/Mantova)
from playwright.sync_api import sync_playwright
U='file:///mnt/user-data/outputs/soto_slug_tex_edition.html'
START="(a)=>{PROG.tut=true; selChar=a[0]; ST.char=a[0]; ST.stage=a[1]; ST.startPart=a[2]||1; MAP={from:null,to:a[1],t:0,fire:false}; mapStart(); setGod(true); for(let i=0;i<200;i++) update(); PL.chute=false; PL.air=false; PL.jy=0; ST.wavePlan=[]; ST.dogPlan=[]; ST.ev=null; enemies=[]; return civs.map(c=>c.col).join('');}"
RUN="""()=>{ const cols={}; for(let i=0;i<9000;i++){ if(ST.trafT>60) ST.trafT=60; update(); for(const v of traffic) cols[v.col]=1; if(ST.bossIn) break; } return Object.keys(cols).sort().join(''); }"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':800}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U); pg.wait_for_timeout(1300); print('version',pg.evaluate("VERSION"))
    parked=''.join(pg.evaluate(START,[0,1+i%3,1]) for i in range(24)); print('500 never parked','p' not in parked)
    for st,nm in [(2,'Genova'),(1,'Lione'),(3,'Marsiglia'),(4,'Mantova')]:
        pg.evaluate(START,[0,st,1]); print(nm,'traffic',pg.evaluate(RUN))
    print('ERR',errs); b.close()
