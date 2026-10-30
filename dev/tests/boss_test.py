from playwright.sync_api import sync_playwright
from PIL import Image
import io,sys
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}"); oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    pg.evaluate("()=>{gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc0'); pg.click('#toStage'); pg.click('#lc1'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()")
    pg.wait_for_timeout(1500)
    shots=[]
    for city in (1,2,4,3):
        r=pg.evaluate("""(c)=>{ST.stage=c;ST.part=c===3?2:1;resetRun(ST.part);PL.chute=false;PL.air=false;PL.jy=0;spawnEnemy=()=>{};enemies=[];ST.scrollX=ST.maxScroll;PL.x=ST.scrollX+300;spawnBoss();setGod(true);
          const t=enemies.find(e=>e.type===5); t.x=ST.scrollX+12; t.st='idle'; t.wait=5; t.hp=t.max*.45; return t.V.style}""",city)
        seen=set(); hp0=None
        for i in range(70):
            pg.wait_for_timeout(100); st=pg.evaluate("()=>{const t=enemies.find(e=>e.type===5);return t?[t.st,t.wounded,eshots.length,(t.marks||[]).length]:null}")
            if st: seen.add(st[0])
            if st and st[0] in ('volley','spread','ram','barrage') and len(shots)<12 and i%3==0:
                shots.append(Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+150,'width':480,'height':380}))))
        print(city,r,'states seen',sorted(seen),'bossbar',pg.evaluate("()=>document.getElementById('bossbar').className"))
    o=Image.new('RGB',(480*6,760)); [o.paste(im,((i%6)*480,(i//6)*380)) for i,im in enumerate(shots[:12])]; o.save(OUT+'boss.png')
    print('ERR',errs); b.close()
