# 1.3.0.64: phones - large text by default, taller pads in portrait, turn-the-phone notice, refit after a zero-size start
from playwright.sync_api import sync_playwright
SP='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/ui/'
U='file:///mnt/user-data/outputs/soto_slug_tex_edition.html'
M="()=>{const c=document.getElementById('cv').getBoundingClientRect(),k=document.getElementById('cab').getBoundingClientRect();return {canvas:[Math.round(c.width),Math.round(c.height)],cab:[Math.round(k.left),Math.round(k.right),Math.round(k.top),Math.round(k.bottom)],pr:getComputedStyle(document.getElementById('cab')).getPropertyValue('--pr'),big:SET.big,bigtxt:document.body.classList.contains('bigtxt'),rot:document.getElementById('rot').classList.contains('on'),mode:ST.mode,sw:document.documentElement.scrollWidth,iw:innerWidth}}"
with sync_playwright() as p:
    b=p.chromium.launch(); errs=[]
    for w,h in [(360,640),(375,812),(390,844),(412,915)]:
        ctx=b.new_context(viewport={'width':w,'height':h},is_mobile=True,has_touch=True,device_scale_factor=2); pg=ctx.new_page(); pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.goto(U); pg.wait_for_timeout(1200); r=pg.evaluate(M); print('portrait',w,h,r)
        if (w,h)==(390,844):
            pg.evaluate("()=>{PROG.tut=true;selChar=0;ST.char=0;ST.stage=2;MAP={from:null,to:2,t:0,fire:false};mapStart();}"); pg.wait_for_timeout(4500); pg.screenshot(path=SP+'p64_portrait.png')
            pg.set_viewport_size({'width':844,'height':390}); pg.wait_for_timeout(600); print('landscape',pg.evaluate(M)); pg.screenshot(path=SP+'p64_land.png')
            pg.click('#rotGo'); pg.wait_for_timeout(300); print('play anyway',pg.evaluate(M))
            pg.set_viewport_size({'width':390,'height':844}); pg.wait_for_timeout(400); print('back portrait',pg.evaluate(M))
        ctx.close()
    # saved choice respected: big off stays off
    ctx=b.new_context(viewport={'width':390,'height':844},is_mobile=True,has_touch=True); pg=ctx.new_page(); pg.goto(U); pg.wait_for_timeout(800)
    pg.evaluate("()=>{SET.big=false;saveSet();}"); pg.reload(); pg.wait_for_timeout(800); print('big off kept',pg.evaluate("()=>[SET.big,document.body.classList.contains('bigtxt')]")); ctx.close()
    # desktop unaffected
    ctx=b.new_context(viewport={'width':1280,'height':800}); pg=ctx.new_page(); pg.goto(U); pg.wait_for_timeout(800); print('desktop',pg.evaluate(M)); ctx.close()
    # zero-size start (page opened in background): must refit once the size is known
    ctx=b.new_context(viewport={'width':390,'height':844},is_mobile=True,has_touch=True); pg=ctx.new_page()
    pg.add_init_script("Object.defineProperty(window,'innerWidth',{get(){return window.__z?0:document.documentElement.clientWidth},configurable:true}); window.__z=true;")
    pg.goto(U); pg.wait_for_timeout(700); a=pg.evaluate(M); pg.evaluate("()=>{window.__z=false}"); pg.wait_for_timeout(700); print('zero start',a['canvas'],'->',pg.evaluate(M)['canvas']); ctx.close()
    print('ERR',errs); b.close()
