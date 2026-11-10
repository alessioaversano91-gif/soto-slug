# 1.3.0.86: Albi's new side-view sheets in every pose, model pose in the character select
from playwright.sync_api import sync_playwright
SP='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/ui/'
U='file:///mnt/user-data/outputs/soto_slug_tex_edition.html'
START="(a)=>{PROG.tut=true; selChar=a[0]; ST.char=a[0]; ST.stage=a[1]; ST.startPart=1; MAP={from:null,to:a[1],t:0,fire:false}; mapStart(); setGod(true); for(let i=0;i<200;i++) update(); PL.chute=false; PL.air=false; PL.jy=0; ST.wavePlan=[]; ST.dogPlan=[]; ST.ev=null; enemies=[]; civs=[]; scn=[]; obs=[]; traffic=[];}"
STATES={'idle':"",'run':"PL.walking=true;PL.t=11;",'walk+fire':"PL.walking=true;PL.fireAnim=20;",'fire':"PL.fireAnim=10;",'crouch':"PL.crouch=true;",'jump':"PL.air=true;PL.vy=-3;PL.jy=-60;",
 'diag':"PL.aimUpT=14;PL.upA=-.8;",'up':"PL.aimUpT=14;PL.upA=-1.3;",'throw':"PL.bombT=8;PL.bombMax=16;",'hurt':"PL.hurtT=8;",'stun':"PL.stunT=20;",'win':"ST.bossDead=true;"}
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':800}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U); pg.wait_for_timeout(1500); print('version',pg.evaluate("VERSION"),'select pose',pg.evaluate("()=>menuIdle(CHARS[0],0)"))
    pg.evaluate(START,[0,2])
    oy=pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'; return document.getElementById('cv').getBoundingClientRect().top}")
    from PIL import Image; ims=[]
    for nm,js in STATES.items():
        k=pg.evaluate("()=>{ Object.assign(PL,{walking:false,fireAnim:0,crouch:false,air:false,jy:0,vy:0,aimUpT:0,bombT:0,hurtT:0,stunT:0,t:7}); ST.bossDead=false; "+js+" const p=gunPose(CHARS[0]); const m=muzzle(); render(); return [p&&p[0],Math.round(m[0]-PL.x),Math.round(m[1]-GROUND)]; }")
        print(nm,k); pg.screenshot(path=SP+'_a_%d.png'%__import__('os').getpid(),clip={'x':0,'y':oy+300,'width':300,'height':200}); ims.append(Image.open(SP+'_a_%d.png'%__import__('os').getpid()).copy())
    o=Image.new('RGB',(300*6,400))
    for i,im in enumerate(ims): o.paste(im,((i%6)*300,(i//6)*200))
    o.save(SP+'albi86.png')
    print('ERR',errs); b.close()
