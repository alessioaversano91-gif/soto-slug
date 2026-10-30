from playwright.sync_api import sync_playwright
from PIL import Image
import io
def start(pg,stage,ch=0):
    pg.evaluate("()=>{gTitle()}"); pg.keyboard.press('Enter'); pg.click(f'#cc{ch}'); pg.click('#toStage'); pg.click(f'#lc{stage-1}'); pg.click('#goBtn'); pg.evaluate("()=>{if(ST.mode==='map')mapStart()}"); pg.wait_for_timeout(400)
    pg.evaluate("()=>{ST.frame=400;enemies=[];obs=[];spawnEnemy=()=>{};}")
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(1000)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}")
    for st in (1,2,3):
        start(pg,st); print('stage',st,'carPlan',pg.evaluate("()=>ST.carPlan.map(c=>c.side>0?'destra':'sinistra')"),'dogPlan',pg.evaluate("()=>ST.dogPlan.map(c=>c.side>0?'destra':'sinistra')"))
    start(pg,1)
    oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    shots=[]
    def snap(): shots.append(Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+200,'width':480,'height':300}))))
    # CAR 1 — from the right
    pg.evaluate("()=>{ST.scrollX=Math.round(ST.maxScroll*.28)+2;PL.x=ST.scrollX+150;PL.dir=1;ST.dmgTaken=0;}")
    pg.wait_for_timeout(250); c1=pg.evaluate("()=>cars.length?{dir:cars[0].dir,st:cars[0].st}:null"); snap()
    pg.wait_for_timeout(450); snap()
    pg.wait_for_timeout(900); park=pg.evaluate("()=>({st:cars[0].st,x:Math.round(cars[0].x-ST.scrollX),player:Math.round(PL.x-ST.scrollX)})"); snap()
    n=pg.evaluate("""()=>new Promise(res=>{let shotsFired=0;const iv=setInterval(()=>{if(shots.length===0&&PL.shootCd<=0)shotsFired++;K.s=1;
        if(cars[0].st!=='park'){clearInterval(iv);K.s=0;res({state:cars[0].st,hp:cars[0].hp,score:ST.score})}},16);setTimeout(()=>{clearInterval(iv);K.s=0;res('timeout')},8000)})""")
    pg.wait_for_timeout(300); snap(); pg.wait_for_timeout(900); snap()
    gone=pg.evaluate("()=>({cars:cars.length,decals:decals.length,dmg:ST.dmgTaken})")
    print('car from right:',c1,'parked',park,'after fire:',n,'later',gone)
    # CAR 2 — from the left, parks behind the player
    pg.evaluate("()=>{cars=[];ST.scrollX=Math.round(ST.maxScroll*.60)+2;PL.x=ST.scrollX+300;PL.dir=1;}")
    pg.wait_for_timeout(1700); c2=pg.evaluate("()=>cars.length?{dir:cars[0].dir,st:cars[0].st,x:Math.round(cars[0].x-ST.scrollX),player:Math.round(PL.x-ST.scrollX)}:null"); snap()
    # shooting from inside the car outline must pass through
    pg.evaluate("()=>{PL.x=cars[0].x;PL.dir=1;window.__hp=cars[0].hp;}"); pg.keyboard.down('z'); pg.wait_for_timeout(400); pg.keyboard.up('z')
    print('car from left:',c2,'| fire from inside outline: hp',pg.evaluate("()=>__hp"),'->',pg.evaluate("()=>cars[0].hp"),'| player damage from cars:',pg.evaluate("()=>ST.dmgTaken"))
    # DOG — Genova
    start(pg,2,0); pg.evaluate("()=>{PL.x=ST.scrollX+200;}")
    sides=[]
    for f in (.18,.48,.78):
        pg.evaluate(f"()=>{{enemies=enemies.filter(e=>e.type!==7);ST.scrollX=Math.round(ST.maxScroll*{f})+2;PL.x=ST.scrollX+220;}}"); pg.wait_for_timeout(120)
        sides.append(pg.evaluate("()=>{const d=enemies.find(e=>e.type===7);return d?(d.dir<0?'da destra':'da sinistra'):null}"))
    print('dog appearances:',sides,'remaining plan',pg.evaluate("()=>ST.dogPlan.length"))
    # bites over 6 s with the player standing still
    pg.evaluate("()=>{enemies=[];ST.dmgTaken=0;spawnDog(1);}")
    shots2=[]
    for i in range(6):
        pg.wait_for_timeout(330); shots2.append(Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+300,'width':480,'height':200}))))
    pg.wait_for_timeout(4000); bites=pg.evaluate("()=>ST.dmgTaken")
    # pounce dodged by jumping
    pg.evaluate("()=>{const d=enemies.find(e=>e.type===7);d.x=PL.x+60;d.dir=-1;dogSet(d,'growl');ST.dmgTaken=0;}")
    pg.wait_for_timeout(560); pg.keyboard.press('x'); pg.wait_for_timeout(900); jumpd=pg.evaluate("()=>ST.dmgTaken")
    # crouch fire kills it
    pg.evaluate("()=>{const d=enemies.find(e=>e.type===7);d.x=PL.x+120;d.dir=-1;dogSet(d,'growl');d.cd=999;PL.dir=1;}")
    pg.keyboard.down('ArrowDown'); pg.keyboard.down('z'); pg.wait_for_timeout(700); pg.keyboard.up('z'); pg.keyboard.up('ArrowDown')
    shots2.append(Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+300,'width':480,'height':200})))); pg.wait_for_timeout(900)
    dead=pg.evaluate("()=>({alive:enemies.filter(e=>e.type===7&&e.hp>0).length,corpse:corpses.some(c=>c.key==='dog_death2')})")
    shots2.append(Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+300,'width':480,'height':200}))))
    print('bites in ~6 s standing still:',bites,'dmg | pounce while jumping:',jumpd,'| crouch fire:',dead,'ERR',errs)
    for name,arr,w,h in (('cd_car.png',shots,480,300),('cd_dog.png',shots2,480,200)):
        out=Image.new('RGB',(240*len(arr),h//2))
        for i,s in enumerate(arr): out.paste(s.resize((240,h//2)),(i*240,0))
        out.save(name)
    b.close()
