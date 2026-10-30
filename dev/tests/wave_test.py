from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc0'); pg.click('#toStage'); pg.click('#lc0'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()")
    pg.wait_for_timeout(1500)
    for city in (2,1,4,3):
        r=pg.evaluate("""(c)=>{ST.stage=c;ST.part=1;resetRun(1);PL.chute=false;PL.air=false;PL.jy=0;setGod(true);return [diff(),JSON.stringify(ST.wavePlan)]}""",city)
        pg.evaluate("()=>{ST.scrollX=ST.wavePlan[0]*ST.maxScroll+2;PL.x=ST.scrollX+200;enemies=[];ST.carPlan=[];ST.dogPlan=[];ST.trevPlan=[]}"); pg.wait_for_timeout(200)
        a=pg.evaluate("()=>[!!ST.wave,ST.lockCam,document.getElementById('flash').textContent]")
        pg.wait_for_timeout(5000)
        n=pg.evaluate("()=>[ST.wave&&ST.wave.q,enemies.filter(e=>e.wave&&e.hp>0).length, enemies.filter(e=>e.wave).map(e=>e.max)]")
        pg.evaluate("()=>{for(const e of enemies) if(e.hp>0&&e.type!==5){e.hp=0;killEnemy(e)}}"); pg.wait_for_timeout(600)
        z=pg.evaluate("()=>[!!ST.wave,ST.lockCam,document.getElementById('flash').textContent]")
        print(city,'diff/plan',r,'start',a,'queue/alive/hp',n,'end',z)
    print('ERR',errs); b.close()
