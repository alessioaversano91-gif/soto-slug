from playwright.sync_api import sync_playwright
from PIL import Image
import io
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(1000)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}")
    pg.keyboard.press('Enter'); pg.click('#cc4'); pg.click('#toStage'); pg.click('#lc2')
    card=pg.evaluate("()=>document.querySelector('#lc2 .ld').textContent")
    pg.click('#goBtn'); pg.evaluate("()=>{if(ST.mode==='map')mapStart()}"); pg.wait_for_timeout(500)
    oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    grab=lambda: Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy,'width':480,'height':640}))).resize((240,320))
    shots=[]
    print('card:',card,'| part',pg.evaluate("()=>ST.part"),'HUD',pg.evaluate("()=>document.getElementById('hst').textContent"))
    pg.evaluate("()=>{spawnEnemy=()=>{};enemies=[];cars=[];ST.carPlan=[];ST.score=4321;ST.scrollX=ST.maxScroll;PL.x=ST.scrollX+200;}")
    pg.wait_for_timeout(250); a=pg.evaluate("()=>({partT:ST.partT,boss:ST.bossIn,enemies:enemies.length})"); shots.append(grab())
    pg.wait_for_timeout(1100); shots.append(grab())
    pg.wait_for_timeout(700)
    b2=pg.evaluate("()=>({part:ST.part,hud:document.getElementById('hst').textContent,score:ST.score,scroll:ST.scrollX,boss:ST.bossIn,carPlan:ST.carPlan.length,mode:ST.mode})")
    shots.append(grab())
    print('end of part 1:',a,'| after transition:',b2)
    pg.wait_for_timeout(1500); shots.append(grab())
    pg.evaluate("()=>{spawnEnemy=()=>{};}")
    for f in (.33,.66):
        pg.evaluate(f"()=>{{ST.scrollX=Math.round(ST.maxScroll*{f});PL.x=ST.scrollX+200;cars=[];}}"); pg.wait_for_timeout(300); shots.append(grab())
    pg.evaluate("()=>{enemies=[];cars=[];ST.scrollX=ST.maxScroll;PL.x=ST.scrollX+260;}"); pg.wait_for_timeout(2600)
    boss=pg.evaluate("()=>{const e=enemies.find(e=>e.type===5);return {name:document.getElementById('bbl').textContent,pre:e&&e.pre,part:ST.part}}"); shots.append(grab())
    pg.evaluate("()=>{const e=enemies.find(e=>e.type===5);e.hp=1;PL.dir=-1;}"); pg.keyboard.down('z'); pg.wait_for_timeout(500); pg.keyboard.up('z'); pg.wait_for_timeout(4500)
    print('boss part 2:',boss,'| mode after boss:',pg.evaluate("()=>ST.mode"),'score',pg.evaluate("()=>ST.score"))
    # other stages untouched
    for st in (1,2):
        pg.evaluate("()=>{gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc0'); pg.click('#toStage'); pg.click(f'#lc{st-1}'); pg.click('#goBtn'); pg.evaluate("()=>{if(ST.mode==='map')mapStart()}"); pg.wait_for_timeout(300)
        pg.evaluate("()=>{spawnEnemy=()=>{};enemies=[];ST.scrollX=ST.maxScroll;PL.x=ST.scrollX+200;}"); pg.wait_for_timeout(600)
        print('stage',st,'HUD',pg.evaluate("()=>document.getElementById('hst').textContent"),'boss spawned',pg.evaluate("()=>ST.bossIn"),'partT',pg.evaluate("()=>ST.partT"))
    out=Image.new('RGB',(240*len(shots),320))
    for i,s in enumerate(shots): out.paste(s,(i*240,0))
    out.save('mars2_journey.png'); print('ERR',errs); b.close()
