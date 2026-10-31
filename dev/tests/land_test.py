from playwright.sync_api import sync_playwright
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
with sync_playwright() as p:
    b=p.chromium.launch()
    for vp,name in (({'width':844,'height':390},'land'),({'width':390,'height':844},'port')):
        pg=b.new_page(viewport=vp,has_touch=True,is_mobile=True,device_scale_factor=2); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(1000)
        pg.evaluate("()=>{PROG.tut=true;gTitle()}"); pg.evaluate("()=>{ if(document.getElementById('rot').classList.contains('on')) document.getElementById('rotGo').click(); }"); pg.keyboard.press('Enter'); pg.click('#cc0'); pg.click('#toStage'); pg.click('#lc0'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()"); pg.wait_for_timeout(1500)
        pg.screenshot(path=OUT+f'{name}.png')
        r=pg.evaluate("()=>{const c=document.getElementById('cv').getBoundingClientRect(),f=document.querySelector('.ab.fire').getBoundingClientRect(),d=document.getElementById('dpad').getBoundingClientRect();return {cv:[c.x|0,c.y|0,c.width|0,c.height|0],fire:[f.x|0,f.y|0,f.width|0],dpad:[d.x|0,d.y|0,d.width|0]}}")
        print(name,r,errs); pg.close()
    b.close()
