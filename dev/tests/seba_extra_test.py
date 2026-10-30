from playwright.sync_api import sync_playwright
from PIL import Image
import io
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(1000)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}"); oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    pg.screenshot(path=OUT+'t_title41.png',clip={'x':0,'y':oy+180,'width':480,'height':260})
    pg.keyboard.press('Enter'); pg.wait_for_timeout(300); pg.screenshot(path=OUT+'t_cards41.png',clip={'x':0,'y':oy,'width':480,'height':560})
    pg.click('#cc1'); pg.click('#toStage'); pg.click('#lc1'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()"); pg.wait_for_timeout(250)
    pg.evaluate("()=>{spawnEnemy=()=>{};enemies=[];obs=[];ST.carPlan=[];ST.dogPlan=[];ST.frame=400;PL.x=ST.scrollX+300;lights=[];AMB.birds=[];ST.mode='paused';PL.inv=0;document.getElementById('scr').classList.add('off');PL.hasUzi=true;updWpnIcon();dropItem(ST.scrollX+420,GROUND-5,'uzi')}")
    shots=[]
    R="PL.fireAnim=0;PL.flashT=0;PL.walking=false;PL.crouch=false;PL.air=false;PL.jy=0;PL.vy=0;PL.melee=0;PL.hurtT=0;PL.reloadT=0;PL.bombT=0;PL.stunT=0;PL.landT=0;PL.dead=false;ST.bossDead=false;PL.dir=1;PL.hasUzi=true;"
    for js in ("PL.bombMax=16;PL.bombT=14","PL.bombMax=16;PL.bombT=8","PL.bombMax=16;PL.bombT=2","PL.crouch=true;PL.bombMax=16;PL.bombT=4","PL.air=true;PL.jy=-80;PL.bombMax=16;PL.bombT=8",
               "PL.meleeKind='punch';PL.meleeMax=18;PL.melee=16","PL.meleeKind='punch';PL.meleeMax=18;PL.melee=12","PL.meleeKind='punch';PL.meleeMax=18;PL.melee=6","PL.crouch=true;PL.meleeKind='lpunch';PL.meleeLow=true;PL.meleeMax=14;PL.melee=8",
               "PL.stunT=20","PL.stunT=10","PL.landT=5","ST.bossDead=true;ST.frame=0","ST.bossDead=true;ST.frame=32",
               "PL.dead=true;PL.lastHurt='drop';PL.deadT=5","PL.dead=true;PL.deadT=20","PL.dead=true;PL.deadT=60","PL.hasUzi=false;PL.dead=true;PL.deadT=60"):
        pg.evaluate("()=>{"+R+js+";render()}"); pg.wait_for_timeout(40)
        x=pg.evaluate("()=>PL.x-ST.scrollX"); im=Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+290,'width':480,'height':210}))); c=im.crop((int(x)-100,0,int(x)+160,210))
        for yy in range(0,210,2): c.putpixel((100,yy),(255,0,0))
        shots.append(c)
    o=Image.new('RGB',(260*6,630)); [o.paste(s,((i%6)*260,(i//6)*210)) for i,s in enumerate(shots)]; o.save(OUT+'seba_extra_states.png')
    pg.screenshot(path=OUT+'t_hud41.png',clip={'x':0,'y':oy+590,'width':480,'height':50})
    print('ERR',errs); b.close()
