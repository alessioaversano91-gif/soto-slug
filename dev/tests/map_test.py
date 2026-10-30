from playwright.sync_api import sync_playwright
from PIL import Image
import io
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(1000)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}")
    oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    grab=lambda: Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy,'width':480,'height':640})))
    pg.keyboard.press('Enter'); pg.click('#cc0'); pg.click('#toStage')
    order=pg.evaluate("()=>[...document.querySelectorAll('#lgr .lc')].map(b=>b.querySelector('.ln').textContent+' '+b.querySelector('.ld').textContent)")
    pg.screenshot(path='map_ls.png',clip={'x':0,'y':oy,'width':480,'height':640})
    print('stage select order:',order)
    pg.click('#lc1'); pg.click('#goBtn'); pg.wait_for_timeout(900)
    s1=grab(); print('after goBtn mode',pg.evaluate("()=>[ST.mode,MAP.from,MAP.to]"))
    pg.keyboard.press('Enter'); pg.wait_for_timeout(400)
    print('Genova start:',pg.evaluate("()=>({mode:ST.mode,city:ST.stage,hud:document.getElementById('hst').textContent,hudVisible:document.getElementById('hud').style.visibility})"))
    pg.evaluate("()=>{spawnEnemy=()=>{};enemies=[];ST.carPlan=[];ST.dogPlan=[];ST.scrollX=ST.maxScroll;PL.x=ST.scrollX+260;}"); pg.wait_for_timeout(2600)
    print('boss 1 (Genova) hp',pg.evaluate("()=>{const e=enemies.find(e=>e.type===5);return e&&[e.max,e.pre,e.waitBase]}"))
    pg.evaluate("()=>{doWin()}"); print('win button:',pg.evaluate("()=>document.getElementById('nextBtn').textContent"))
    pg.click('#nextBtn'); pg.wait_for_timeout(1300); s2=grab(); pg.wait_for_timeout(1500); s3=grab()
    print('route map:',pg.evaluate("()=>[MAP.from,MAP.to,mapArrived()]"))
    pg.mouse.click(240,oy+300); pg.wait_for_timeout(400)
    print('Lione start:',pg.evaluate("()=>({mode:ST.mode,city:ST.stage,hud:document.getElementById('hst').textContent})"))
    # boss difficulty along the journey
    res=[]
    for city in (2,1,4,3):
        pg.evaluate(f"()=>{{ST.stage={city};ST.part=2;enemies=[];spawnTank();}}"); res.append(pg.evaluate("()=>{const e=enemies.find(e=>e.type===5);return CITY[ST.stage].name+':'+e.max+'hp/'+e.waitBase}"))
    print('bosses in journey order:',res)
    # after Marsiglia -> tour map -> new round from Genova
    pg.evaluate("()=>{enemies=[];ST.stage=3;ST.part=2;doWin();}"); print('last win button:',pg.evaluate("()=>document.getElementById('nextBtn').textContent"))
    pg.click('#nextBtn'); pg.wait_for_timeout(700); s4=grab(); print('tour map:',pg.evaluate("()=>MAP.to"))
    pg.keyboard.press('Enter'); pg.wait_for_timeout(300); print('after tour ->',pg.evaluate("()=>[ST.mode,MAP.from,MAP.to]"))
    # FIRE button (touch) continues too
    pg.wait_for_timeout(300); pg.evaluate("()=>{K.s=1}"); pg.wait_for_timeout(100); pg.evaluate("()=>{K.s=0}"); pg.wait_for_timeout(200)
    pg.evaluate("()=>{ST.credT=200}"); pg.evaluate("()=>{K.s=1}"); pg.wait_for_timeout(100)
    print('FIRE on map/credits ->',pg.evaluate("()=>[ST.mode]"),'(expect credits then title)','ERR',errs)
    out=Image.new('RGB',(4*480+30,640),(0,0,0))
    for i,s in enumerate([s1,s2,s3,s4]): out.paste(s,(i*490,0))
    out.resize((out.width//2,320)).save('map_views.png'); s3.save('map_arrive.png')
    b.close()
