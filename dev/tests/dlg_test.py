from playwright.sync_api import sync_playwright
from PIL import Image
import io
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}"); oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    pg.evaluate("()=>{gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc2'); pg.click('#toStage'); pg.click('#lc0'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()")
    pg.wait_for_timeout(1800)
    pg.evaluate("()=>{PL.chute=false;PL.air=false;PL.jy=0;enemies=[];ST.scrollX=ST.maxScroll;PL.x=ST.scrollX+300;setGod(true)}"); pg.wait_for_timeout(1800)
    a=Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy,'width':480,'height':640})))
    print('dlg',pg.evaluate("()=>[document.getElementById('dlg').className,document.getElementById('dlgt').textContent]"))
    pg.evaluate("()=>{enemies=[];ST.bossIn=false;ST.lockCam=false;dropItem(PL.x,GROUND,'sg');}"); pg.wait_for_timeout(500)
    c=Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy,'width':480,'height':640})))
    o=Image.new('RGB',(960,640)); o.paste(a,(0,0)); o.paste(c,(480,0)); o.save(OUT+'dlg.png')
    print('ERR',errs); b.close()
