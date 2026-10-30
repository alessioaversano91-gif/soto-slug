from playwright.sync_api import sync_playwright
def c(bb): return bb['x']+bb['width']/2, bb['y']+bb['height']/2
with sync_playwright() as p:
    b=p.chromium.launch()
    for vw,vh,name in [(560,900,'desk'),(390,844,'phone')]:
        pg=b.new_page(viewport={'width':vw,'height':vh},has_touch=(name=='phone'))
        errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.evaluate("()=>{document.body.classList.remove('kb');fit()}"); pg.wait_for_timeout(100); pg.wait_for_timeout(900)
        pg.keyboard.press('Enter');pg.click('#cc0');pg.click('#toStage');pg.click('#lc0');pg.click('#goBtn'); pg.evaluate("()=>{if(ST.mode==='map')mapStart()}");pg.wait_for_timeout(3000)
        pg.evaluate("()=>{spawnEnemy=()=>{};enemies=[];obs=[];PL.x=ST.scrollX+240}")
        sz=pg.evaluate("()=>Object.fromEntries([...document.querySelectorAll('#dpad .dz, #pad .ab')].map(e=>{const r=e.getBoundingClientRect();return [e.dataset.k,Math.round(r.width)+'x'+Math.round(r.height)]}))")
        L,J,D,R=[pg.locator(f'#dpad .dz[data-k={k}]').bounding_box() for k in 'ljdr']
        F=pg.locator('#pad .ab[data-k=s]').bounding_box()
        # 1 slide L -> D -> R without lifting
        x0=pg.evaluate("()=>PL.x"); pg.mouse.move(*c(L)); pg.mouse.down(); pg.wait_for_timeout(350); xl=pg.evaluate("()=>PL.x")
        pg.mouse.move(*c(D),steps=5); pg.wait_for_timeout(150); cr=pg.evaluate("()=>PL.crouch")
        pg.mouse.move(*c(R),steps=5); pg.wait_for_timeout(350); xr=pg.evaluate("()=>PL.x")
        pg.mouse.up(); pg.wait_for_timeout(80); rel=pg.evaluate("()=>K.l+K.r+K.d")
        # 2 tap ▲ alone: jump in place
        pg.mouse.move(*c(J)); pg.mouse.down(); pg.wait_for_timeout(60); pg.mouse.up(); pg.wait_for_timeout(200)
        j1=pg.evaluate("()=>({air:PL.air,jy:Math.round(PL.jy)})"); pg.wait_for_timeout(900)
        # 3 running jump: hold ▶ then slide up to ▲ (one thumb)
        pg.mouse.move(*c(R)); pg.mouse.down(); pg.wait_for_timeout(300); xa=pg.evaluate("()=>PL.x")
        pg.mouse.move(*c(J),steps=4); pg.wait_for_timeout(250)
        rj=pg.evaluate("()=>({air:PL.air,r:K.r})"); pg.wait_for_timeout(450); xb=pg.evaluate("()=>PL.x"); pg.mouse.up()
        # 4 holding ▲ must give ONE jump
        pg.wait_for_timeout(900); pg.evaluate("()=>{window.__n=0;let pa=false;window.__iv=setInterval(()=>{if(PL.air&&!pa)__n++;pa=PL.air},16)}")
        pg.mouse.move(*c(J)); pg.mouse.down(); pg.wait_for_timeout(2000); pg.mouse.up(); jumps=pg.evaluate("()=>{clearInterval(__iv);return __n}")
        # 5 fire
        pg.mouse.move(*c(F)); pg.mouse.down(); pg.wait_for_timeout(250); fired=pg.evaluate("()=>PL.fireAnim>0||shots.length>0"); pg.mouse.up()
        print(name,'sizes',sz)
        print(f'  1 slide L>D>R: left {round(xl-x0)}  crouch-on-D {cr}  right {round(xr-xl)}  keys-after-release {rel}')
        print(f'  2 tap jump: {j1}   3 running jump R->J: {rj} advanced {round(xb-xa)}px   4 hold J 2s -> jumps {jumps}   5 fire {fired}  ERR {errs}')
        if name=='phone': pg.screenshot(path='t_pad_phone.png')
        pg.close()
    b.close()
