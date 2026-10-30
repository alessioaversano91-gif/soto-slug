from playwright.sync_api import sync_playwright
from PIL import Image
import io
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(1000)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}")
    pg.keyboard.press('Enter'); pg.click('#cc2'); pg.click('#toStage'); pg.click('#lc3'); pg.wait_for_timeout(200)
    pg.screenshot(path='mantova_ls.png',clip={'x':0,'y':0,'width':480,'height':640})
    pg.click('#goBtn'); pg.evaluate("()=>{if(ST.mode==='map')mapStart()}"); pg.wait_for_timeout(600)
    oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    grab=lambda: Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy,'width':480,'height':640}))).resize((240,320))
    shots=[grab()]
    info=pg.evaluate("()=>({stage:ST.stage,hud:document.getElementById('hst').textContent,label:getBG(4).label,cars:ST.carPlan.length,dogs:ST.dogPlan.length})")
    types=pg.evaluate("""()=>{const c={};ST.gendNext=0;for(let i=0;i<800;i++){ST.frame+=110;ST.scrollX=(i%100)/100*ST.maxScroll;enemies=[];spawnEnemy();for(const e of enemies)c[e.type]=(c[e.type]||0)+1;}enemies=[];return c;}""")
    print('start:',info,'| enemy types spawned in 800 calls:',types)
    pg.evaluate("()=>{spawnEnemy=()=>{};enemies=[];}")
    for f in (.33,.66):
        pg.evaluate(f"()=>{{ST.scrollX=Math.round(ST.maxScroll*{f});PL.x=ST.scrollX+200;}}"); pg.wait_for_timeout(300); shots.append(grab())
    pg.evaluate("()=>{ST.scrollX=ST.maxScroll;PL.x=ST.scrollX+260;}"); pg.wait_for_timeout(2600)
    boss=pg.evaluate("()=>{const e=enemies.find(e=>e.type===5);return {name:document.getElementById('bbl').textContent,pre:e&&e.pre,hp:e&&e.max}}"); shots.append(grab())
    pg.evaluate("()=>{const e=enemies.find(e=>e.type===5);e.hp=1;PL.dir=-1;}"); pg.keyboard.down('z'); pg.wait_for_timeout(500); pg.keyboard.up('z'); pg.wait_for_timeout(4500)
    print('boss:',boss,'| mode:',pg.evaluate("()=>ST.mode"))
    pg.click('#nextBtn'); pg.evaluate("()=>{if(ST.mode==='map')mapStart()}"); pg.wait_for_timeout(300); print('next stage after Mantova ->',pg.evaluate("()=>ST.stage"))
    pg.evaluate("()=>{ST.stage=3;ST.part=2;doWin();}"); pg.click('#nextBtn'); pg.evaluate("()=>{if(ST.mode==='map')mapStart()}"); pg.wait_for_timeout(300); print('next stage after Marsiglia ->',pg.evaluate("()=>[ST.stage,document.getElementById('hst').textContent]"))
    out=Image.new('RGB',(240*len(shots),320))
    for i,s in enumerate(shots): out.paste(s,(i*240,0))
    out.save('mantova_journey.png'); print('ERR',errs); b.close()
