from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{PROG.tut=true;gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc1'); pg.click('#toStage'); pg.click('#lc0'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()")
    pg.wait_for_timeout(1500)
    pg.evaluate("()=>{PL.chute=false;PL.air=false;PL.jy=0;enemies=[];ST.scrollX=ST.maxScroll;PL.x=ST.scrollX+250;setGod(true)}"); pg.wait_for_timeout(1200)
    print('music',pg.evaluate("()=>musicWant()"))
    pg.evaluate("()=>{const t=enemies.find(e=>e.type===5);t.hp=t.max*.4}"); pg.wait_for_timeout(300); print('music phase2',pg.evaluate("()=>[musicWant(),enemies.find(e=>e.type===5).wounded]"))
    print('boss kill',pg.evaluate("()=>{const t=enemies.find(e=>e.type===5);t.hp=0;killEnemy(t);const f0=ST.frame;for(let i=0;i<20;i++)update();return [ST.hitStop,ST.slowT,ST.frame-f0]}"))
    print('ERR',errs); b.close()
