from playwright.sync_api import sync_playwright
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
with sync_playwright() as p:
    b=p.chromium.launch(); ctx=b.new_context(viewport={'width':480,'height':900},accept_downloads=True); pg=ctx.new_page(); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}"); oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    pg.evaluate("()=>{PROG.tut=true;gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc2'); pg.click('#toStage'); pg.click('#lc0'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()")
    pg.wait_for_timeout(2500); pg.keyboard.press('p'); pg.wait_for_timeout(300)
    with pg.expect_download() as d: pg.click('#photoPause')
    d.value.save_as(OUT+'photo.png'); print('download',d.value.suggested_filename)
    pg.keyboard.press('p'); pg.evaluate("()=>{PL.chute=false;PL.air=false;PL.jy=0;enemies=[];ST.scrollX=ST.maxScroll;PL.x=ST.scrollX+250}"); pg.wait_for_timeout(1000)
    pg.evaluate("()=>{const t=enemies.find(e=>e.type===5);t.hp=0;killEnemy(t);ST.bossT=1}"); pg.wait_for_timeout(5000)
    pg.screenshot(path=OUT+'winpanel.png',clip={'x':0,'y':oy,'width':480,'height':640})
    pg.click('#titleBtn'); pg.click('#rankBtn'); pg.wait_for_timeout(200); pg.screenshot(path=OUT+'stats.png',clip={'x':0,'y':oy,'width':480,'height':640})
    print(pg.evaluate("()=>JSON.stringify(PROG.st)"))
    print('ERR',errs); b.close()
