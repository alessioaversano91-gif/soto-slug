from playwright.sync_api import sync_playwright
from PIL import Image
import io
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':640})
    errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(1000)
    pg.evaluate("()=>{document.getElementById('wrap').style.transform='none'}")
    pg.keyboard.press('Enter'); pg.click('#cc0'); pg.click('#toStage'); pg.click('#lc0'); pg.click('#goBtn'); pg.evaluate("()=>{if(ST.mode==='map')mapStart()}")
    pg.evaluate("()=>{ST.frame=400;spawnEnemy=()=>{};enemies=[];obs=[];}")
    pg.wait_for_timeout(300)
    def grab(): return Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':290,'width':480,'height':190})))
    strip=[]
    def snapPL(label):
        x=pg.evaluate("()=>PL.x-ST.scrollX"); im=grab(); strip.append(im.crop((max(0,int(x)-70),0,max(0,int(x)-70)+140,190)))
    pg.keyboard.down('ArrowRight')
    for i in range(6): pg.wait_for_timeout(85); snapPL('R')
    pg.keyboard.up('ArrowRight'); pg.keyboard.down('ArrowLeft')
    for i in range(4): pg.wait_for_timeout(85); snapPL('L')
    pg.keyboard.up('ArrowLeft'); pg.wait_for_timeout(200); snapPL('idle')
    pg.keyboard.down('ArrowDown'); pg.wait_for_timeout(150); snapPL('crouch')
    pg.keyboard.down('z'); pg.wait_for_timeout(120); snapPL('crouchfire'); pg.keyboard.up('z'); pg.keyboard.up('ArrowDown')
    pg.evaluate("()=>{PL.dir=1;}"); pg.keyboard.down('z'); pg.wait_for_timeout(120); snapPL('fire'); pg.keyboard.up('z'); pg.wait_for_timeout(400)
    # melee: put a bottle right in front
    pg.evaluate("()=>{const s=S.bottle;enemies.push({type:0,key:'bottle',x:PL.x+22,y:GROUND-(s.h+12),w:s.w,h:s.h+12,hp:20,max:20,dir:-1,vx:0,t:0,shootT:9999,flash:0,keep:0,hoverY:0});PL.shootCd=0;}")
    pg.keyboard.down('z')
    for i in range(3): pg.wait_for_timeout(95); snapPL('punch')
    pg.keyboard.up('z'); pg.wait_for_timeout(300)
    pg.keyboard.down('ArrowDown'); pg.evaluate("()=>{PL.shootCd=0;enemies[0].x=PL.x+22}"); pg.keyboard.down('z')
    for i in range(2): pg.wait_for_timeout(100); snapPL('lpunch')
    pg.keyboard.up('z'); pg.keyboard.up('ArrowDown')
    pg.evaluate("()=>{PL.hurtT=10}"); pg.wait_for_timeout(40); snapPL('hurt')
    W=140*len(strip); out=Image.new('RGB',(W,190))
    for i,s in enumerate(strip): out.paste(s,(i*140,0))
    out.crop((0,0,140*10,190)).save('albi_strip1.png'); out.crop((140*10,0,W,190)).save('albi_strip2.png')
    print('ERR',errs, pg.evaluate("()=>({hp:enemies.map(e=>e.hp),score:ST.score})"))
    b.close()
