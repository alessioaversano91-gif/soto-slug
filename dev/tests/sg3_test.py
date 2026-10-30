from playwright.sync_api import sync_playwright
from PIL import Image
import io
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}"); oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    pg.evaluate("()=>{gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc2'); pg.click('#toStage'); pg.click('#lc1'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()")
    pg.wait_for_timeout(300); pg.evaluate("()=>{PL.chute=false;PL.air=false;PL.jy=0;spawnEnemy=()=>{};enemies=[];obs=[];ST.carPlan=[];ST.dogPlan=[];falls=[];ST.dropT=99999;PL.inv=0;setGod(false);setSG(true);PL.sgAmmo=20}")
    # death with shotgun keeps it for the animation, then it's gone after respawn
    pg.evaluate("()=>{PL.hp=1;PL.inv=0;hurtPlayer('drop',PL.x,GROUND-80)}"); pg.wait_for_timeout(300)
    print('dying: sg set in hand',pg.evaluate("()=>[PL.dead,CHARS[ST.char].gun===CHARS[ST.char].sg]"))
    pg.wait_for_timeout(4000); print('after respawn: sg?',pg.evaluate("()=>[PL.dead,sgOn(),PL.sgAmmo]"))
    pg.evaluate("()=>{setSG(true);PL.sgAmmo=20;ST.mode='paused';PL.x=ST.scrollX+300;lights=[];parts=[];corpses=[];items=[];AMB.birds=[];shots=[];enemies=[]}")
    R="PL.fireAnim=0;PL.flashT=0;PL.walking=false;PL.crouch=false;PL.air=false;PL.jy=0;PL.vy=0;PL.melee=0;PL.hurtT=0;PL.pickT=0;PL.bombT=0;PL.stunT=0;PL.landT=0;PL.apT=0;PL.aimUpT=0;PL.aimDnT=0;PL.idleLong=0;PL.dead=false;ST.bossDead=false;PL.dir=1;PL.meleeLow=false;PL.back=false;PL.inv=0;PL.hitT=0;"
    sh=[]
    for js in ["PL.walking=true;PL.t=0","PL.walking=true;PL.t=5","PL.walking=true;PL.t=10","PL.walking=true;PL.t=15","ST.bossDead=true;ST.frame=0","ST.bossDead=true;ST.frame=16","PL.stunT=20","PL.hurtT=6",
               "PL.bombMax=16;PL.bombT=8","PL.meleeKind='punch';PL.meleeMax=18;PL.melee=16","PL.meleeKind='punch';PL.meleeMax=18;PL.melee=10","PL.dead=true;PL.lastHurt='drop';PL.deadT=12","PL.dead=true;PL.lastHurt='drop';PL.deadT=26","PL.dead=true;PL.lastHurt='drop';PL.deadT=60","PL.t=0"]:
        pg.evaluate("()=>{"+R+js+";render()}"); pg.wait_for_timeout(40)
        x=pg.evaluate("()=>PL.x-ST.scrollX"); im=Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+290,'width':480,'height':210}))); c=im.crop((int(x)-110,0,int(x)+130,210))
        for yy in range(0,210,2): c.putpixel((110,yy),(255,0,0))
        sh.append(c)
    o=Image.new('RGB',(240*8,420)); [o.paste(s,((i%8)*240,(i//8)*210)) for i,s in enumerate(sh)]; o.save(OUT+'sg3_states.png')
    print('ERR',errs); b.close()
