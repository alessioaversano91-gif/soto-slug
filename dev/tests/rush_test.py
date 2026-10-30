from playwright.sync_api import sync_playwright
from PIL import Image
import io
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}"); oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    pg.evaluate("()=>{gTitle()}"); pg.wait_for_timeout(200); pg.screenshot(path=OUT+'r_title.png',clip={'x':0,'y':oy,'width':480,'height':640})
    pg.click('#rushBtn'); pg.click('#cc1'); pg.click('#toStage'); pg.wait_for_timeout(1500)
    print('rush start',pg.evaluate("()=>[ST.mode,ST.stage,ST.part,ST.bossIn,!!ST.rush,document.getElementById('hst').textContent]"))
    for i in range(4):
        pg.evaluate("()=>{const t=enemies.find(e=>e.type===5); if(t){t.hp=0;killEnemy(t);}}"); pg.wait_for_timeout(200)
        # fast-forward the victory delay
        pg.evaluate("()=>{ST.bossT=1;}"); pg.wait_for_timeout(1900)
        print(i,pg.evaluate("()=>[ST.mode,ST.stage,ST.rush&&ST.rush.i,ST.bossIn,document.getElementById('hst').textContent]"))
        pg.wait_for_timeout(600)
    print('final',pg.evaluate("()=>[ST.mode,document.getElementById('winstats').textContent,document.getElementById('recWin').className,JSON.stringify(PROG.med)]"))
    pg.fill('#recWinIn','tester'); pg.click('#recWinBtn')
    print('saved',pg.evaluate("()=>[JSON.stringify(PROG.board),JSON.stringify(PROG.rush)]"))
    pg.screenshot(path=OUT+'r_win.png',clip={'x':0,'y':oy,'width':480,'height':640})
    pg.click('#titleBtn'); pg.wait_for_timeout(200); pg.click('#rankBtn'); pg.wait_for_timeout(200); pg.screenshot(path=OUT+'r_rank.png',clip={'x':0,'y':oy,'width':480,'height':640})
    pg.click('#rankBack'); pg.click('#medBtn'); pg.wait_for_timeout(200); pg.screenshot(path=OUT+'r_med.png',clip={'x':0,'y':oy,'width':480,'height':640})
    # part selection
    pg.click('#medBack'); pg.keyboard.press('Enter'); pg.click('#cc0'); pg.click('#toStage'); pg.click('#lc2'); pg.click('#partBtn'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()"); pg.wait_for_timeout(300)
    print('part select ->',pg.evaluate("()=>[ST.stage,ST.part,!!ST.rush]"))
    # game over record
    pg.evaluate("()=>{ST.score=123456;ST.lives=0;gameOver()}"); pg.wait_for_timeout(100)
    print('gameover record form',pg.evaluate("()=>document.getElementById('recGo').className"))
    pg.keyboard.type('zzz'); pg.keyboard.press('Enter'); pg.wait_for_timeout(100)
    print('typed into input / mode',pg.evaluate("()=>[ST.mode,JSON.stringify(PROG.board.map(r=>r.n))]"))
    print('ERR',errs); b.close()
