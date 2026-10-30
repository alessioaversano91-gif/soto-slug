from playwright.sync_api import sync_playwright
from PIL import Image
import io
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}"); oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    pg.evaluate("()=>{PROG.tut=true;gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc0'); pg.click('#toStage'); pg.click('#lc2'); pg.click('#partBtn'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()")
    pg.wait_for_timeout(2500)
    pg.evaluate("()=>{spawnEnemy=()=>{};enemies=[];setGod(true);PL.chute=false;PL.air=false;PL.jy=0;dropItem(PL.x+40,GROUND-80,'rapid')}"); pg.wait_for_timeout(200)
    pg.evaluate("()=>{const it=items.find(i=>i.kind==='rapid'); if(it){it.y=GROUND;it.land=true;PL.x=it.x}}"); pg.wait_for_timeout(300)
    print('rapid',pg.evaluate("()=>[ST.powT,document.getElementById('flash').textContent]"))
    print('cd halved',pg.evaluate("()=>{PL.shootCd=0;PL.melee=0;enemies=[];doShoot();return PL.shootCd}"))
    pg.screenshot(path=OUT+'pow.png',clip={'x':0,'y':oy+200,'width':480,'height':330})
    pg.evaluate("()=>{ST.scrollX=ST.maxScroll*.28+3;PL.x=ST.scrollX+200;ST.wavePlan=[];ST.trevPlan=[]}"); pg.wait_for_timeout(2000)
    print('salvo',pg.evaluate("()=>[!!ST.salvo,ST.marks.length,document.getElementById('flash').textContent]"))
    pg.screenshot(path=OUT+'salvo.png',clip={'x':0,'y':oy+200,'width':480,'height':330})
    pg.wait_for_timeout(4000); print('salvo end',pg.evaluate("()=>[!!ST.salvo,ST.marks.length,ST.dmgTaken]"))
    print('ERR',errs); b.close()
