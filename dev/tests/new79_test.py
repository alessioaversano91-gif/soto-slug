# 1.3.0.79: Marseille part 2 picked from the menu starts fresh (bombs were NaN); medal toast away from the combo meter; long flashes wrap
from playwright.sync_api import sync_playwright
U='file:///mnt/user-data/outputs/soto_slug_tex_edition.html'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U); pg.wait_for_timeout(1500); print('version',pg.evaluate("VERSION"))
    for ch in (0,4):
        pg.evaluate("()=>{PROG.tut=true;gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc%d'%ch); pg.click('#toStage'); pg.click('#lc2'); pg.click('#partBtn')
        print('label',pg.inner_text('#partBtn')); pg.click('#goBtn'); pg.evaluate("()=>mapStart()"); pg.wait_for_timeout(300)
        print('char',ch,pg.evaluate("()=>({part:ST.part,bombs:ST.bombs,hud:document.getElementById('hbombs').textContent,kills:ST.kills,used:ST.bombsUsed})"))
    pg.evaluate("()=>{ award(Object.keys(MEDALS||{})[0]||'nodmg'); }") if pg.evaluate("()=>typeof MEDALS!=='undefined'") else pg.evaluate("()=>award('nodmg')")
    pg.wait_for_timeout(400)
    print('toast left', pg.evaluate("()=>{const r=document.getElementById('toast').getBoundingClientRect(), c=document.getElementById('cv').getBoundingClientRect(); return Math.round(r.left-c.left)<20 && r.right-c.left<300;}"))
    print('flash wraps', pg.evaluate("()=>{ flash('ATTENZIONE: CARRO CHARTREUSE GIALLA ALLE SPALLE!'); const e=document.getElementById('flash'); return e.getBoundingClientRect().height>12; }"))
    print('ERR',errs); b.close()
