# Beta: the file opened on its own (no Claude around) - downloads, saves, labels, head metadata
from playwright.sync_api import sync_playwright
U='file:///mnt/user-data/outputs/soto_slug_tex_edition.html'
with sync_playwright() as p:
    b=p.chromium.launch(); ctx=b.new_context(viewport={'width':1280,'height':800},accept_downloads=True); pg=ctx.new_page(); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U); pg.wait_for_timeout(1200)
    print('claude object:',pg.evaluate("()=>typeof window.claude"))
    print('title/label:',pg.evaluate("()=>[document.title,document.getElementById('lgv').textContent,!!document.querySelector('link[rel=icon]'),!!document.querySelector('link[rel=apple-touch-icon]')]"))
    pg.evaluate("()=>{PROG.tut=true;selChar=0;ST.char=0;ST.stage=2;MAP={from:null,to:2,t:0,fire:false};mapStart();}"); pg.wait_for_timeout(2500)
    pg.keyboard.press('p'); pg.wait_for_timeout(200)
    with pg.expect_download(timeout=8000) as d: pg.click('#photoPause')
    print('photo download:',d.value.suggested_filename)
    pg.evaluate("()=>{togglePause();gTitle();openSettings()}")
    with pg.expect_download(timeout=8000) as d: pg.click('#expBtn')
    print('export download:',d.value.suggested_filename)
    pg.reload(); pg.wait_for_timeout(1200); print('saves kept after reload:',pg.evaluate("()=>[PROG.tut===true,localStorage.getItem('sotoProg')!==null]"))
    print('ERR',errs); b.close()
