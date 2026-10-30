# Automatic check run by build.sh after every build: loads the game, walks the menus, and lets the bot
# finish two levels. Exit code 1 (and a FAIL line) if anything breaks.
from playwright.sync_api import sync_playwright
import sys
exec(open('bot_test.py').read().split('god=(')[0])          # reuses the BOT driver
fails=[]
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    try:
        pg.evaluate("()=>{PROG.tut=true;gTitle()}")
        for btn,back in (('#medBtn','#medBack'),('#rankBtn','#rankBack')): pg.click(btn); pg.click(back)
        pg.click('#setBtn'); pg.click('#keysBtn'); pg.click('#keysBack'); pg.click('#setBackBtn')
        pg.keyboard.press('Enter'); pg.click('#cc0'); pg.click('#toStage'); pg.click('#lc0'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()"); pg.wait_for_timeout(800)
        if pg.evaluate("()=>ST.mode")!='playing': fails.append('menus: did not reach the game')
    except Exception as e: fails.append('menus: '+str(e)[:120])
    if errs: fails.append('page errors: '+'; '.join(errs[:3]))
    pg.close()
    for c,s in ((0,2),(2,3),(4,4)):
        pg=b.new_page(viewport={'width':480,'height':700}); errs=[]; pg.on('pageerror',lambda e,errs=errs:errs.append(str(e)))
        pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(700)
        r=pg.evaluate(BOT,[c,s,True])
        if r['mode']!='win' or r['notes'] or errs: fails.append(f"bot char {c} city {s}: {r['mode']} {r['notes'][:1]} {errs[:2]}")
        pg.close()
    b.close()
print('QUICK CHECK '+('PASS' if not fails else 'FAIL'))
for f in fails: print('  - '+f)
sys.exit(1 if fails else 0)
