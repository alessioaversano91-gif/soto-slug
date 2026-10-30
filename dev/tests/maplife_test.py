from playwright.sync_api import sync_playwright
from PIL import Image
import io
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(1000)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}")
    oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    pg.keyboard.press('Enter'); pg.click('#cc1'); pg.click('#toStage'); pg.click('#lc0'); pg.click('#goBtn'); pg.evaluate("()=>{if(ST.mode==='map')mapStart()}"); pg.wait_for_timeout(300)
    pg.evaluate("()=>{doWin()}"); pg.click('#nextBtn'); pg.wait_for_timeout(50)
    shots=[]
    for T in (9,24,95,260):
        pg.evaluate(f"()=>{{MAP.t={T}}}"); pg.wait_for_timeout(34)
        shots.append(Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+56,'width':480,'height':340}))))
    info=pg.evaluate("()=>[MAP.from,MAP.to]")
    pg.evaluate("()=>{ST.stage=3;ST.part=2;showMap(3,'tour');MAP.t=200}"); pg.wait_for_timeout(60)
    shots.append(Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+56,'width':480,'height':340}))))
    # ship really moves
    a=pg.evaluate("()=>{MAP.t=100;return 0}"); pg.wait_for_timeout(1500)
    print('map',info,'ERR',errs)
    for i,s in enumerate(shots): s.save(f'maplife_{i}.png')
    out=Image.new('RGB',(480*2+10,340*2+10),(0,0,0))
    for i,s in enumerate(shots[1:5]): out.paste(s,((i%2)*490,(i//2)*350))
    out.save('maplife_grid.png')
    b.close()
