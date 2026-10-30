from playwright.sync_api import sync_playwright
from PIL import Image
import io
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}"); oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    pg.evaluate("()=>{PROG.tut=true;gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc4'); pg.click('#toStage'); pg.click('#lc0'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()")
    pg.wait_for_timeout(2500)
    pg.evaluate("()=>{spawnEnemy=()=>{};enemies=[];setGod(true);PL.x=ST.scrollX+120;PL.dir=1;const s=S.bottle;for(const dx of [90,170]) enemies.push({type:0,key:'bottle',x:PL.x+dx,y:GROUND-(s.h+12),w:s.w,h:s.h+12,hp:30,max:30,dir:-1,vx:0,t:0,shootT:9999,flash:0,keep:0,hoverY:0});}")
    pg.evaluate("()=>{PL.shootCd=0;doShoot()}")
    log=[]; ims=[]
    for i in range(16):
        pg.wait_for_timeout(110)
        log.append(pg.evaluate("()=>{const a=shots.find(q=>q.k==='axe');return [a?Math.round(a.x-PL.x):null,a?a.back?1:0:'-',PL.catchT||0,enemies.map(e=>e.hp)]}"))
        if i in (2,5,8,11): ims.append(Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+250,'width':480,'height':250}))))
    print(log)
    print('second throw blocked while flying?',pg.evaluate("()=>{PL.shootCd=0;doShoot();const n1=PL.throwT;return n1}"))
    o=Image.new('RGB',(960,500)); [o.paste(im,((i%2)*480,(i//2)*250)) for i,im in enumerate(ims)]; o.save(OUT+'boom.png')
    print('ERR',errs); b.close()
