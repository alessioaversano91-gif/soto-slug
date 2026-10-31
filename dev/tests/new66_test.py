# 1.3.0.66: Genova in three levels (Porto Antico, Corso Italia, Stazione Principe)
from playwright.sync_api import sync_playwright
SP='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/ui/'
U='file:///mnt/user-data/outputs/soto_slug_tex_edition.html'
WIN="()=>{ ST.wavePlan=[]; ST.dogPlan=[]; ST.ev=null; enemies=[]; PL.chute=false; PL.air=false; PL.jy=0; ST.scrollX=ST.maxScroll; PL.x=ST.scrollX+250; for(let i=0;i<300;i++) update(); const t=enemies.find(e=>e.type===5); if(t){ t.hp=0; killEnemy(t); } for(let i=0;i<400&&ST.mode==='playing';i++) update(); return [ST.mode,ST.stage,ST.part,document.getElementById('nextBtn').textContent]; }"
with sync_playwright() as p:
    b=p.chromium.launch(); ctx=b.new_context(viewport={'width':480,'height':900}); pg=ctx.new_page(); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U); pg.wait_for_timeout(1200)
    pg.evaluate("()=>{PROG.tut=true;saveProg();gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc0'); pg.click('#toStage'); pg.click('#lc1')
    labels=[pg.evaluate("()=>document.getElementById('partBtn').textContent")]
    for i in range(3): pg.click('#partBtn'); labels.append(pg.evaluate("()=>document.getElementById('partBtn').textContent"))
    print('part button',labels)
    pg.click('#goBtn'); pg.evaluate("()=>mapStart()"); pg.wait_for_timeout(600)
    for lvl in (1,2):
        print('level',lvl,pg.evaluate("()=>[ST.stage,ST.part,stageTag(),document.getElementById('hst').textContent]"))
        pg.evaluate("()=>{ for(let i=0;i<150;i++) update(); render(); }"); pg.screenshot(path=f'{SP}gen_l{lvl}.png',clip={'x':0,'y':0,'width':480,'height':640})
        print('  win',pg.evaluate(WIN),pg.evaluate("()=>[...document.querySelectorAll('#winstats .obj')].map(d=>d.textContent)"))
        print('  resume',pg.evaluate("()=>JSON.stringify(PROG.resume).slice(0,90)"))
        pg.click('#nextBtn'); pg.wait_for_timeout(400)
    print('level 3',pg.evaluate("()=>[ST.stage,ST.part,stageTag(),document.getElementById('hst').textContent]"))
    pg.evaluate("()=>{ for(let i=0;i<150;i++) update(); render(); }"); pg.screenshot(path=f'{SP}gen_l3.png',clip={'x':0,'y':0,'width':480,'height':640})
    # continue after closing the page mid-Genova
    pg2=ctx.new_page(); pg2.on('pageerror',lambda e:errs.append(str(e)))
    pg2.goto(U); pg2.wait_for_timeout(1200); print('cont btn',pg2.evaluate("()=>document.getElementById('contBtn').textContent"))
    pg2.click('#contBtn'); pg2.wait_for_timeout(300); pg2.evaluate("()=>mapStart()"); pg2.wait_for_timeout(300); print('resumed at',pg2.evaluate("()=>[ST.stage,ST.part,stageTag()]")); pg2.close()
    print('  win 3',pg.evaluate(WIN),pg.evaluate("()=>[...document.querySelectorAll('#winstats .obj')].map(d=>d.textContent.trim())"))
    pg.click('#nextBtn'); pg.wait_for_timeout(300); print('after Genova',pg.evaluate("()=>[ST.mode,MAP.from,MAP.to]"))
    print('ERR',errs); b.close()
