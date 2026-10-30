from playwright.sync_api import sync_playwright
from PIL import Image
import io
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}"); oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    pg.evaluate("()=>{gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc0'); pg.click('#toStage'); pg.click('#lc2'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()")
    pg.wait_for_timeout(2500)
    print('stage/part/plan',pg.evaluate("()=>[ST.stage,ST.part,JSON.stringify(ST.trevPlan)]"))
    pg.evaluate("()=>{spawnEnemy=()=>{};enemies=[];PL.air=false;PL.chute=false;PL.jy=0;ST.scrollX=ST.maxScroll*.3+5;PL.x=ST.scrollX+150;PL.inv=9999;setGod(true)}")
    ims=[]; log=[]
    for i in range(14):
        pg.wait_for_timeout(330); st=pg.evaluate("()=>TRV?[TRV.st,Math.round(TRV.x-ST.scrollX),ST.lockCam,enemies.filter(e=>e.type===6).map(e=>e.hp)]:['none',0,ST.lockCam,enemies.filter(e=>e.type===6).map(e=>e.hp)]"); log.append(st)
        ims.append(Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+200,'width':480,'height':330}))))
    print(log)
    print('flash',pg.evaluate("()=>document.getElementById('flash').textContent"))
    # shots pass through Trevor? kill gendarmes
    pg.evaluate("()=>{enemies.filter(e=>e.type===6).forEach(e=>{e.hp=0;killEnemy(e)})}"); pg.wait_for_timeout(2500)
    print('after kill: fight/lock',pg.evaluate("()=>[ST.trevFight,ST.lockCam,document.getElementById('flash').textContent,TRV&&TRV.st]"))
    o=Image.new('RGB',(480*7,660)); [o.paste(im,((i%7)*480,(i//7)*330)) for i,im in enumerate(ims)]; o.save(OUT+'trev_seq.png')
    # pass-by
    pg.evaluate("()=>{TRV=null;spawnTrevor('pass')}"); pg.wait_for_timeout(700); pg.screenshot(path=OUT+'trev_pass.png',clip={'x':0,'y':oy+200,'width':480,'height':330})
    print('ERR',errs); b.close()
