# 1.3.0.90: Albi's parachute (hang, fire, land), mid-air shot down and 3-frame air throw
from playwright.sync_api import sync_playwright
SP='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/ui/'
U='file:///mnt/user-data/outputs/soto_slug_tex_edition.html'
START=open('new86_test.py').read().split('START="')[1].split('"\n')[0]
RST="Object.assign(PL,{walking:false,fireAnim:0,crouch:false,air:false,chute:false,paraLand:false,landT:0,jy:0,vy:0,aimUpT:0,aimDnT:0,bombT:0,hurtT:0,stunT:0,t:7});"
STATES={'chute':"PL.chute=true;PL.air=true;PL.jy=-40;",'chute+fire':"PL.chute=true;PL.air=true;PL.jy=-40;PL.fireAnim=10;",
 'land0':"PL.paraLand=true;PL.landT=30;",'land1':"PL.paraLand=true;PL.landT=4;",'airdown':"PL.air=true;PL.jy=-80;PL.vy=1;PL.aimDnT=10;",
 'jthrow0':"PL.air=true;PL.jy=-80;PL.bombT=15;PL.bombMax=16;",'jthrow1':"PL.air=true;PL.jy=-80;PL.bombT=8;PL.bombMax=16;",'jthrow2':"PL.air=true;PL.jy=-80;PL.bombT=2;PL.bombMax=16;"}
EXP={'chute':'albi_n_para0','chute+fire':'albi_n_para0','land0':'albi_n_paraland','land1':'albi_n_paraready','airdown':'albi_n_jdn','jthrow0':'albi_n_jthrow0','jthrow1':'albi_n_jthrow1','jthrow2':'albi_n_jthrow2'}
ok=True
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':800}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U); pg.wait_for_timeout(1500); print('version',pg.evaluate("VERSION"))
    pg.evaluate(START,[0,2])
    oy=pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'; return document.getElementById('cv').getBoundingClientRect().top}")
    from PIL import Image; ims=[]
    for nm,js in STATES.items():
        k=pg.evaluate("()=>{ "+RST+" ST.bossDead=false; "+js+" const p=gunPose(CHARS[0]); const m=muzzle(); render(); return [p&&p[0],Math.round(m[0]-PL.x),Math.round(m[1]-(GROUND+PL.jy))]; }")
        good=bool(k[0]) and k[0].startswith(EXP[nm]); ok&=good; print(nm,k,'OK' if good else 'FAIL')
        pg.screenshot(path=SP+'_a.png',clip={'x':0,'y':oy+180,'width':300,'height':320}); ims.append(Image.open(SP+'_a.png').copy())
    o=Image.new('RGB',(300*4,640))
    for i,im in enumerate(ims): o.paste(im,((i%4)*300,(i//4)*320))
    o.save(SP+'albi90.png')
    # real descent at level start: chute pose, then landing sequence, no errors
    pg.evaluate("()=>{selChar=0; ST.char=0; ST.stage=2; ST.startPart=1; MAP={from:null,to:2,t:0,fire:false}; mapStart(); setGod(true);}")
    seen=pg.evaluate("()=>{const s=new Set(); for(let i=0;i<400;i++){ update(); const p=gunPose(CHARS[0]); if(p) s.add(p[0]); } return [...s].filter(k=>k.includes('para'));}")
    print('descent',seen); ok&= 'albi_n_para0' in seen and 'albi_n_paraready' in seen
    print('ERR',errs); ok&=not errs; b.close()
print('PASS' if ok else 'FAIL')
