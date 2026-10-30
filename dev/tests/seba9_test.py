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
    pg.wait_for_timeout(1500); ims.append(Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+60,'width':480,'height':580}))))
    while pg.evaluate("()=>PL.air"): pg.wait_for_timeout(30)
    pg.wait_for_timeout(100); ims.append(Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+60,'width':480,'height':580}))))
    # with UZI: replay the parachute
    pg.evaluate("()=>{spawnEnemy=()=>{};enemies=[];PL.hasUzi=true;updWpnIcon();PL.air=true;PL.jy=-300;PL.vy=0;PL.chute=true;PL.inv=0}")
    pg.wait_for_timeout(1200); ims.append(Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+60,'width':480,'height':580}))))
    while pg.evaluate("()=>PL.air"): pg.wait_for_timeout(30)
    pg.wait_for_timeout(100); ims.append(Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+60,'width':480,'height':580}))))
    pg.evaluate("()=>{PL.porHitT=40;updPortrait()}"); pg.wait_for_timeout(60); ims.append(Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+60,'width':480,'height':580}))))
    o=Image.new('RGB',(480*5,580)); [o.paste(im,(i*480,0)) for i,im in enumerate(ims)]; o.save(OUT+'s9_chute.png')
    pg.evaluate("()=>{ST.mode='paused';PL.x=ST.scrollX+300;lights=[];parts=[];items=[];AMB.birds=[];PL.walking=false;PL.fireAnim=0;PL.landT=0;PL.paraLand=false;PL.hurtT=0;PL.inv=0}")
    sh=[]
    for v in (118,90,62,40,10):
        pg.evaluate("()=>{PL.idleLong=%d;render()}"%v); pg.wait_for_timeout(40)
        x=pg.evaluate("()=>PL.x-ST.scrollX"); sh.append(Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+290,'width':480,'height':210}))).crop((int(x)-80,0,int(x)+80,210)))
    o=Image.new('RGB',(160*5,210)); [o.paste(s,(i*160,0)) for i,s in enumerate(sh)]; o.save(OUT+'s9_idle.png')
    print('ERR',errs); b.close()
