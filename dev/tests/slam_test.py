from playwright.sync_api import sync_playwright
from PIL import Image
import io
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}"); oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    pg.evaluate("()=>{PROG.tut=true;gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc4'); pg.click('#toStage'); pg.click('#lc0'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()")
    pg.wait_for_timeout(1500); pg.evaluate("()=>{PL.chute=false;PL.air=false;PL.jy=0;PL.landT=0;spawnEnemy=()=>{};enemies=[];setGod(true);const s=S.bottle;for(const dx of [-60,60]) enemies.push({type:0,key:'bottle',x:PL.x+dx-s.w/2,y:GROUND-(s.h+12),w:s.w,h:s.h+12,hp:30,max:30,dir:-1,vx:0,t:0,shootT:9999,flash:0,keep:0,hoverY:0});}")
    pg.wait_for_timeout(300); pg.keyboard.press('ArrowUp'); pg.wait_for_timeout(250); pg.evaluate("()=>{PL.shootCd=0;doShoot()}")
    sh=[]
    for i in range(8):
        pg.wait_for_timeout(90); x=pg.evaluate("()=>PL.x-ST.scrollX")
        sh.append(Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+220,'width':480,'height':280}))).crop((int(x)-110,0,int(x)+110,280)))
    print(pg.evaluate("()=>[PL.slam,PL.slamLand,enemies.map(e=>e.hp)]"))
    o=Image.new('RGB',(220*8,280)); [o.paste(s,(i*220,0)) for i,s in enumerate(sh)]; o.save(OUT+'slam.png')
    print('ERR',errs); b.close()
