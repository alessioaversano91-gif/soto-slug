from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); ctx=b.new_context(viewport={'width':480,'height':900}); pg=ctx.new_page(); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{PROG.tut=true;saveProg();gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc1'); pg.click('#toStage'); pg.click('#lc0'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()")
    pg.wait_for_timeout(1500); pg.evaluate("()=>{setGod(false);PL.chute=false;PL.air=false;PL.jy=0;PL.hasUzi=true;ST.wavePlan=[];ST.carPlan=[];ST.scrollX=ST.maxScroll*.5+5;PL.x=ST.scrollX+200;ST.score=4321}"); pg.wait_for_timeout(500)
    print('saved',pg.evaluate("()=>JSON.stringify(PROG.save)"))
    pg2=ctx.new_page(); pg2.on('pageerror',lambda e:errs.append(str(e))); pg.close()
    pg2.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg2.wait_for_timeout(1000)
    print('title btn',pg2.evaluate("()=>[document.getElementById('contBtn').style.display,document.getElementById('contBtn').textContent]"))
    pg2.click('#contBtn'); pg2.wait_for_timeout(500)
    print('resumed',pg2.evaluate("()=>[ST.mode,ST.stage,CHARS[ST.char].name,Math.round(ST.scrollX/ST.maxScroll*100),ST.score,PL.hasUzi]"))
    pg2.evaluate("()=>{SET.eco=true}"); pg2.wait_for_timeout(1500); print('eco ok',pg2.evaluate("()=>ST.mode"))
    print('ERR',errs); b.close()
