from playwright.sync_api import sync_playwright
from PIL import Image
import io
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}"); oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    pg.evaluate("()=>{PROG.tut=true;gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc3'); pg.click('#toStage'); pg.click('#lc1'); pg.click('#goBtn'); pg.evaluate("()=>{ST.startPart=3;mapStart()}")   # Genova: the tank is only at level 3 (1.3.0.70)
    pg.wait_for_timeout(2000)
    pg.keyboard.down('ArrowRight'); pg.keyboard.down('z'); pg.wait_for_timeout(6000); pg.keyboard.up('ArrowRight'); pg.keyboard.up('z')
    pg.evaluate("()=>{ST.scrollX=ST.maxScroll;PL.x=ST.scrollX+250;ST.wave=null;ST.lockCam=false}"); pg.wait_for_timeout(4200)
    print('reply',pg.evaluate("()=>[document.getElementById('dlgn').textContent,document.getElementById('dlgt').textContent]"))
    pg.screenshot(path=OUT+'reply.png',clip={'x':0,'y':oy+380,'width':480,'height':150})
    pg.evaluate("()=>{const t=enemies.find(e=>e.type===5);t.hp=0;killEnemy(t);ST.bossT=1;award('kills500')}"); pg.wait_for_timeout(2500)
    print(pg.evaluate("()=>document.getElementById('winstats').innerText"))
    pg.screenshot(path=OUT+'sum.png',clip={'x':0,'y':oy,'width':480,'height':640})
    print('ERR',errs); b.close()
