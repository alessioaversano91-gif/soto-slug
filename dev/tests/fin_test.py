from playwright.sync_api import sync_playwright
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}"); oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    pg.evaluate("()=>{PROG.tut=true;ST.char=3;ST.score=234500;MAP={from:3,to:'tour',t:0};mapStart()}"); pg.wait_for_timeout(4200)
    pg.screenshot(path=OUT+'finale.png',clip={'x':0,'y':oy,'width':480,'height':640})
    pg.keyboard.press('Enter'); pg.wait_for_timeout(300); print('after enter',pg.evaluate("()=>ST.mode"))
    print('ERR',errs); b.close()
