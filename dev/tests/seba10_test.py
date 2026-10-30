from playwright.sync_api import sync_playwright
from PIL import Image
import io
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}"); oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    pg.evaluate("()=>{gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc1'); pg.click('#toStage'); pg.click('#lc1'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()")
    ims=[]
    for t in (700,1500):
        pg.wait_for_timeout(t if t==700 else 800); ims.append(Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+100,'width':480,'height':420}))))
    while pg.evaluate("()=>PL.air"): pg.wait_for_timeout(20)
    for d in (60,250,450):
        pg.wait_for_timeout(d if d==60 else 200); ims.append(Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+100,'width':480,'height':420}))))
    o=Image.new('RGB',(480*5,420)); [o.paste(im,(i*480,0)) for i,im in enumerate(ims)]; o.save(OUT+'s10_chute.png')
    pg.evaluate("()=>{spawnEnemy=()=>{};enemies=[];ST.mode='paused';PL.x=ST.scrollX+300;lights=[];parts=[];items=[];AMB.birds=[];PL.inv=0}")
    R="PL.fireAnim=0;PL.walking=false;PL.crouch=false;PL.air=false;PL.jy=0;PL.vy=0;PL.melee=0;PL.hurtT=0;PL.pickT=0;PL.bombT=0;PL.stunT=0;PL.landT=0;PL.paraLand=false;PL.apT=0;PL.idleLong=0;PL.dead=false;ST.bossDead=false;PL.dir=1;PL.hasUzi=false;PL.chute=false;PL.hitT=0;"
    sh=[]
    for js in ["PL.t=0","PL.t=14","PL.idleLong=110","PL.idleLong=80","PL.idleLong=50","PL.hurtT=8","PL.hurtT=3","PL.air=true;PL.jy=-80;PL.vy=2","PL.landT=5","PL.walking=true;PL.t=6"]:
        pg.evaluate("()=>{"+R+js+";render()}"); pg.wait_for_timeout(40)
        x=pg.evaluate("()=>PL.x-ST.scrollX"); c=Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+290,'width':480,'height':210}))).crop((int(x)-90,0,int(x)+90,210))
        for yy in range(0,210,2): c.putpixel((90,yy),(255,0,0))
        sh.append(c)
    o=Image.new('RGB',(180*10,210)); [o.paste(s,(i*180,0)) for i,s in enumerate(sh)]; o.save(OUT+'s10_states.png')
    print('ERR',errs); b.close()
