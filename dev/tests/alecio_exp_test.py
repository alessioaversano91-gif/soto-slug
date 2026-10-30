from playwright.sync_api import sync_playwright
from PIL import Image
import io
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}"); oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    pg.evaluate("()=>{gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc3'); pg.click('#toStage'); pg.click('#lc1'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()")
    seq=[]
    for w in (100,700,1300):
        pg.wait_for_timeout(w if w==100 else 600); seq.append(pg.evaluate("()=>[Math.round(PL.jy),PL.chute,PL.air]"))
    pg.wait_for_timeout(2600); seq.append(pg.evaluate("()=>[Math.round(PL.jy),PL.chute,PL.air,PL.paraLand]"))
    print('parachute entrance jy/chute/air:',seq)
    pg.evaluate("()=>{spawnEnemy=()=>{};enemies=[];obs=[];ST.carPlan=[];ST.dogPlan=[];falls=[];ST.dropT=99999;PL.inv=0;PL.air=false;PL.jy=0;PL.chute=false}")
    # aim up at a flying bottle overhead
    r=pg.evaluate("""()=>{const s=S.bottle_s;enemies=[{type:2,key:'bottle_s',x:PL.x+50,y:GROUND-300,w:s.w,h:s.h,hp:99,max:99,dir:-1,vx:0,t:0,shootT:9999,flash:0,keep:0,hoverY:GROUND-300}];
      shots=[];PL.shootCd=0;PL.dir=1;doShoot();const b=shots[0];return {aimUp:PL.aimUpT,vx:+b.vx.toFixed(1),vy:+b.vy.toFixed(1)}}""")
    print('aim up:',r)
    r=pg.evaluate("""()=>{const s=S.bottle;enemies=[{type:0,key:'bottle',x:PL.x+40,y:GROUND-(s.h+12),w:s.w,h:s.h+12,hp:99,max:99,dir:-1,vx:0,t:0,shootT:9999,flash:0,keep:0,hoverY:0}];
      shots=[];PL.air=true;PL.jy=-110;PL.vy=-1;PL.shootCd=0;PL.aimUpT=0;doShoot();const b=shots[0];return {aimDn:PL.aimDnT,vx:+b.vx.toFixed(1),vy:+b.vy.toFixed(1)}}""")
    print('aim down in jump:',r)
    pg.evaluate("()=>{enemies=[];shots=[];PL.air=false;PL.jy=0;PL.vy=0}")
    # long idle
    pg.wait_for_timeout(6500); print('long idle after ~6.5s:',pg.evaluate("()=>PL.idleLong>0||PL.idleT<50"))
    # portrait
    pg.evaluate("()=>{PL.inv=0;hurtPlayer('drop',PL.x,300)}"); pg.wait_for_timeout(100); h=pg.evaluate("()=>PL.porKey"); pg.wait_for_timeout(1000); n=pg.evaluate("()=>PL.porKey")
    print('portrait hit/normal:',h,n)
    pg.evaluate("()=>{ST.mode='paused';PL.x=ST.scrollX+300;lights=[];parts=[];AMB.birds=[];AMB.rain=[];document.getElementById('scr').classList.add('off')}")
    shots=[]
    R="PL.fireAnim=0;PL.flashT=0;PL.walking=false;PL.crouch=false;PL.air=false;PL.jy=0;PL.vy=0;PL.melee=0;PL.hurtT=0;PL.pickT=0;PL.bombT=0;PL.landT=0;PL.paraLand=false;PL.chute=false;PL.aimUpT=0;PL.aimDnT=0;PL.idleLong=0;PL.dir=1;"
    for js in ("PL.aimUpT=10;PL.fireAnim=10;PL.flashT=3","PL.aimUpT=10;PL.walking=true;PL.t=0;PL.fireAnim=10;PL.flashT=3","PL.aimUpT=10;PL.walking=true;PL.t=6;PL.fireAnim=10","PL.aimUpT=10;PL.air=true;PL.jy=-80;PL.fireAnim=10;PL.flashT=3",
               "PL.aimDnT=10;PL.air=true;PL.jy=-90;PL.fireAnim=10;PL.flashT=3","PL.walking=true;PL.t=0","PL.walking=true;PL.t=5","PL.walking=true;PL.t=10","PL.walking=true;PL.t=15","PL.dir=-1;PL.walking=true;PL.t=5",
               "PL.idleLong=110","PL.idleLong=80","PL.idleLong=50","PL.pickMax=24;PL.pickT=22","PL.pickMax=24;PL.pickT=12","PL.pickMax=24;PL.pickT=3",
               "PL.chute=true;PL.air=true;PL.jy=-150;ST.frame=0","PL.chute=true;PL.air=true;PL.jy=-150;ST.frame=22","PL.landT=15;PL.paraLand=true","PL.bombMax=16;PL.bombT=14","PL.crouch=true;PL.bombMax=16;PL.bombT=4","PL.hurtT=3","PL.dead=true;PL.lastHurt='tankshot';PL.deadT=50","PL.idleLong=20"):
        pg.evaluate("()=>{"+R+js+";render()}"); pg.wait_for_timeout(40)
        x=pg.evaluate("()=>PL.x-ST.scrollX"); im=Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+250,'width':480,'height':250}))); c=im.crop((int(x)-110,0,int(x)+140,250))
        for yy in range(0,250,2): c.putpixel((110,yy),(255,0,0))
        shots.append(c)
    o=Image.new('RGB',(250*8,750)); [o.paste(s,((i%8)*250,(i//8)*250)) for i,s in enumerate(shots)]; o.save(OUT+'alecio_exp_states.png')
    pg.screenshot(path=OUT+'alecio_exp_hud.png',clip={'x':0,'y':oy+580,'width':480,'height':60})
    print('ERR',errs); b.close()
