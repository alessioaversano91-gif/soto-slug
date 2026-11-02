# 1.3.0.74: bigger vehicles, GROUND raised 20 px, traffic enters/leaves fully off screen
from playwright.sync_api import sync_playwright
SP='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/ui/'
U='file:///mnt/user-data/outputs/soto_slug_tex_edition.html'
START="(a)=>{PROG.tut=true; selChar=a[0]; ST.char=a[0]; ST.stage=a[1]; ST.startPart=a[2]||1; MAP={from:null,to:a[1],t:0,fire:false}; mapStart(); setGod(true); for(let i=0;i<200;i++) update(); PL.chute=false; PL.air=false; PL.jy=0; ST.wavePlan=[]; ST.dogPlan=[]; ST.ev=null; enemies=[]; return [GROUND,PL.y|0];}"
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':800}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U); pg.wait_for_timeout(1300); print('version',pg.evaluate("VERSION"))
    oy=pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'; return document.getElementById('cv').getBoundingClientRect().top}")
    for st,pt,tr,nm in [(2,1,'b','gen1'),(2,3,'c','gen3'),(1,1,'t','lione'),(3,1,'f','mars'),(4,1,None,'mantova')]:
        print(nm,pg.evaluate(START,[0,st,pt]))
        pg.evaluate("(tr)=>{ traffic=tr?[{col:tr,dir:1,v:3,x:ST.scrollX-40,t:7}]:[]; if(civs[0]){ civs[0].x=ST.scrollX+250; } PL.x=ST.scrollX+120; render(); }",tr)
        pg.screenshot(path=SP+f'v74_{nm}.png',clip={'x':0,'y':oy,'width':480,'height':640})
    # traffic never pops in: spawned fully off screen, culled fully off screen
    r=pg.evaluate("""()=>{ ST.stage=1; let bad=0,n=0; for(let k=0;k<40;k++){ traffic=[]; ST.trafT=1; updateTraffic(); const v=traffic[0]; if(!v) continue; n++; const w=CVM['civ'+v.col+'_idle'].w; if(v.dir>0? v.x+w>ST.scrollX : v.x<ST.scrollX+W) bad++; } return {n,bad}; }""")
    print('spawn off screen',r)
    print('ERR',errs); b.close()
