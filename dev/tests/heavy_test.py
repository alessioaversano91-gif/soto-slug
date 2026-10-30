from playwright.sync_api import sync_playwright
from PIL import Image
import io
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}"); oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    pg.evaluate("()=>{PROG.tut=true;gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc1'); pg.click('#toStage'); pg.click('#lc0'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()")
    pg.wait_for_timeout(3000)
    while pg.evaluate("()=>PL.air||PL.landT>0"): pg.wait_for_timeout(50)
    pg.evaluate("()=>{spawnEnemy=()=>{};enemies=[];setGod(true);PL.inv=0;hurtPlayer('tankshot',PL.x,GROUND-80)}"); pg.wait_for_timeout(150)
    x=pg.evaluate("()=>PL.x-ST.scrollX"); Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+300,'width':480,'height':200}))).crop((int(x)-90,0,int(x)+90,200)).save(OUT+'heavy.png')
    print(pg.evaluate("()=>[PL.heavyT,PL.stunT]"),'ERR',errs); b.close()
