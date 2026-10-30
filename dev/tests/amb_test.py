from playwright.sync_api import sync_playwright
from PIL import Image
import io
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}"); oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    pg.evaluate("()=>{PROG.tut=true;gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc0'); pg.click('#toStage'); pg.click('#lc0'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()")
    pg.wait_for_timeout(1500); ims=[]
    for c in (2,1,4,3):
        pg.evaluate("(c)=>{ST.stage=c;ST.part=1;resetRun(1);PL.chute=false;PL.air=false;PL.jy=0;spawnEnemy=()=>{};enemies=[];ST.scrollX=ST.maxScroll*.4;PL.x=ST.scrollX+150;ST.wavePlan=[];ST.trevPlan=[];ST.carPlan=[];ST.dogPlan=[]}",c); pg.wait_for_timeout(1200)
        print(c,'water pts',pg.evaluate("()=>Object.fromEntries(Object.entries(WATER).map(([k,v])=>[k,v.length]))"))
        ims.append(Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+40,'width':480,'height':500}))))
    o=Image.new('RGB',(1920,500)); [o.paste(im,(i*480,0)) for i,im in enumerate(ims)]; o.save(OUT+'amb.png')
    print('ERR',errs); b.close()
