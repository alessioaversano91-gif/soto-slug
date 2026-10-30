from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc0'); pg.click('#toStage'); pg.click('#lc1'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()")
    pg.wait_for_timeout(3500); t=lambda: pg.evaluate("()=>[ST.tut&&ST.tut.step,document.getElementById('dlgt').textContent]")
    print(t()); pg.keyboard.down('ArrowRight'); pg.wait_for_timeout(1500); pg.keyboard.up('ArrowRight'); pg.wait_for_timeout(1500); print(t())
    pg.evaluate("()=>{ST.kills=1}"); pg.wait_for_timeout(1500); print(t())
    pg.keyboard.press('ArrowUp'); pg.wait_for_timeout(800); pg.keyboard.down('ArrowDown'); pg.wait_for_timeout(300); pg.keyboard.up('ArrowDown'); pg.wait_for_timeout(1500); print(t())
    pg.keyboard.press('c'); pg.wait_for_timeout(1500); print(t()); pg.wait_for_timeout(4000); print(t(), pg.evaluate("()=>PROG.tut"))
    print('ERR',errs); b.close()
