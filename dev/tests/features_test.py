from playwright.sync_api import sync_playwright
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
URL='file:///mnt/user-data/outputs/soto_slug_tex_edition.html'
def start(pg,ch=0,city=1,god=True):
    pg.evaluate("()=>{gTitle()}"); pg.keyboard.press('Enter'); pg.click(f'#cc{ch}'); pg.click('#toStage'); pg.click(f'#lc{city-1}'); pg.click('#goBtn'); pg.evaluate("()=>{if(ST.mode==='map')mapStart()}"); pg.wait_for_timeout(250)
    pg.evaluate("(g)=>{setGod(g);PL.inv=0;}",god)
def shot(pg,oy,name): pg.screenshot(path=OUT+name,clip={'x':0,'y':oy,'width':480,'height':640})
with sync_playwright() as p:
    b=p.chromium.launch(); ctx=b.new_context(viewport={'width':480,'height':900}); pg=ctx.new_page(); errs=[]; cons=[]
    pg.on('pageerror',lambda e:errs.append(str(e))); pg.on('console',lambda m: cons.append(m.text) if m.type=='error' else None)
    pg.goto(URL); pg.wait_for_timeout(1200)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}"); oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    print('version',pg.evaluate("()=>VERSION"),'| font loaded:',pg.evaluate("()=>document.fonts.check('8px \"Press Start 2P\"')"))
    # A1 settings
    pg.click('#setBtn'); pg.wait_for_timeout(100); a=pg.evaluate("()=>[ST.setOpen,document.getElementById('pset').classList.contains('on')]")
    pg.click('.vb[data-v="mus"][data-d="1"]'); pg.click('.vb[data-v="sfx"][data-d="-1"]'); pg.click('#calmBtn')
    shot(pg,oy,'f_settings.png')
    s1=pg.evaluate("()=>[SET.mus,SET.sfx,SET.calm,localStorage.getItem('sotoSet')]")
    pg.click('#setBackBtn'); back=pg.evaluate("()=>[ST.mode,document.getElementById('pt').classList.contains('on')]")
    print('A1 settings open',a,'| changed',s1,'| back',back)
    pg.click('#setBtn'); pg.click('#calmBtn'); pg.click('#setBackBtn')
    # A7 back + menu arrows
    pg.keyboard.press('Enter'); pg.keyboard.press('ArrowRight'); pg.keyboard.press('ArrowRight'); c1=pg.evaluate("()=>selChar")
    pg.keyboard.press('Enter'); m1=pg.evaluate("()=>ST.mode"); pg.keyboard.press('ArrowRight'); st=pg.evaluate("()=>selStage")
    pg.keyboard.press('Escape'); m2=pg.evaluate("()=>ST.mode"); pg.click('#csBack'); m3=pg.evaluate("()=>ST.mode")
    print('A7 arrows char',c1,'->',m1,'stage',st,'| Esc ->',m2,'| back button ->',m3)
    # A3 gamepad (fake pad)
    pg.evaluate("""()=>{window.__pad={connected:true,buttons:Array.from({length:17},()=>({pressed:false})),axes:[0,0,0,0]};navigator.getGamepads=()=>[window.__pad];}""")
    start(pg,0,1)
    pg.evaluate("()=>{__pad.buttons[15].pressed=true;__pad.buttons[2].pressed=true;}"); pg.wait_for_timeout(120)
    g1=pg.evaluate("()=>[K.r,K.s]")
    pg.evaluate("()=>{__pad.buttons[15].pressed=false;__pad.buttons[2].pressed=false;__pad.buttons[0].pressed=true;}"); pg.wait_for_timeout(60); g2=pg.evaluate("()=>[K.r,K.s,PL.air]")
    pg.evaluate("()=>{__pad.buttons[0].pressed=false;__pad.buttons[9].pressed=true;}"); pg.wait_for_timeout(60); g3=pg.evaluate("()=>ST.mode")
    pg.evaluate("()=>{__pad.buttons[9].pressed=false;}"); pg.wait_for_timeout(60); pg.evaluate("()=>{__pad.buttons[9].pressed=true;}"); pg.wait_for_timeout(60); g4=pg.evaluate("()=>ST.mode")
    pg.evaluate("()=>{__pad.buttons[9].pressed=false;navigator.getGamepads=()=>[]}")
    print('A3 gamepad right+fire',g1,'| A jump',g2,'| START',g3,'-> START',g4)
    # A5 checkpoint (LIFE)
    start(pg,0,2,False); pg.evaluate("()=>{spawnEnemy=()=>{};enemies=[];ST.scrollX=ST.maxScroll*.52;PL.x=ST.scrollX+180;}"); pg.wait_for_timeout(200)
    cp=pg.evaluate("()=>ST.cp&&{x:Math.round(ST.cp.x),part:ST.cp.part}")
    pg.evaluate("()=>{ST.lives=1;PL.hp=1;hurtPlayer('drop',PL.x,300)}"); pg.wait_for_timeout(2300)
    rt=pg.evaluate("()=>[ST.mode,document.getElementById('retryBtn').textContent]"); pg.click('#retryBtn'); pg.wait_for_timeout(150)
    print('A5 checkpoint',cp,'| game over',rt,'| after retry scroll',pg.evaluate("()=>[Math.round(ST.scrollX),ST.lives,ST.mode]"))
    # A4 progress save + C17 city score
    start(pg,0,1); pg.evaluate("()=>{ST.cityStart=0;ST.score=8400;doWin()}"); pg.wait_for_timeout(200)
    print('A4 saved',pg.evaluate("()=>localStorage.getItem('sotoProg')"),'cityScore',pg.evaluate("()=>ST.cityScore"))
    # B9 wounded boss
    start(pg,0,1); pg.evaluate("()=>{spawnEnemy=()=>{};enemies=[];ST.scrollX=ST.maxScroll;}"); pg.wait_for_timeout(2500)
    w0=pg.evaluate("()=>{const e=enemies.find(e=>e.type===5);return e&&{st:e.st,wait:tankWait(e,0)}}")
    pg.evaluate("()=>{const e=enemies.find(e=>e.type===5);e.hp=Math.floor(e.max*.45);}"); pg.wait_for_timeout(900)
    w1=pg.evaluate("()=>{const e=enemies.find(e=>e.type===5);return e&&{wounded:e.wounded,wait:tankWait(e,0)}}")
    shot(pg,oy,'f_boss.png'); print('B9 boss before',w0,'| wounded',w1)
    # B10 bonus crates
    start(pg,0,2); n=pg.evaluate("()=>[obs.filter(o=>o.bonus).length,obs.length]")
    pg.evaluate("()=>{spawnEnemy=()=>{};enemies=[];const o=obs.find(o=>o.bonus);ST.scrollX=Math.max(0,o.x-260);PL.x=o.x-120;ST.lockCam=true;}"); pg.wait_for_timeout(200); shot(pg,oy,'f_crate.png')
    r=pg.evaluate("()=>{const o=obs.find(o=>o.bonus&&o.x>ST.scrollX);const s0=ST.score,i0=items.length;damageOb(o,99);return {items:items.length-i0,score:ST.score-s0}}")
    print('B10 crates (bonus/total)',n,'| destroyed bonus crate ->',r)
    # B11 falling bottles
    start(pg,0,2,False); pg.evaluate("()=>{spawnEnemy=()=>{};enemies=[];ST.frame=400;ST.dropT=1;PL.walking=false;}"); pg.wait_for_timeout(250)
    f1=pg.evaluate("()=>falls.length"); shot(pg,oy,'f_fall_warn.png')
    pg.evaluate("()=>{if(falls[0])falls[0].x=PL.x}"); pg.wait_for_timeout(1500)
    print('B11 falls spawned',f1,'| hp after landing on player',pg.evaluate("()=>PL.hp"))
    # B12 gendarmes from the car
    start(pg,0,1); pg.evaluate("()=>{spawnEnemy=()=>{};enemies=[];spawnCar(1);}"); pg.wait_for_timeout(4200)
    print('B12 car state',pg.evaluate("()=>cars.map(c=>c.st)"),'gendarmes',pg.evaluate("()=>enemies.filter(e=>e.type===6).length")); shot(pg,oy,'f_gend.png')
    # B13 combo
    start(pg,0,2); r=pg.evaluate("()=>{enemies=[];const s0=ST.score;const out=[];for(let i=0;i<7;i++){const e={type:0,x:PL.x+150,y:GROUND-90,w:30,h:90,dir:-1,hp:1};const a=ST.score;killEnemy(e);out.push(ST.score-a);}return {gains:out,combo:ST.combo}}")
    pg.wait_for_timeout(120); shot(pg,oy,'f_combo.png'); print('B13 combo',r)
    # C14/C15 ambience
    start(pg,0,1); pg.evaluate("()=>{AMB.bolt=6}"); pg.wait_for_timeout(300); print('C14/15 Lyon birds/rain',pg.evaluate("()=>[AMB.birds.length,AMB.birds[0].k,AMB.rain.length]")); shot(pg,oy,'f_rain.png')
    start(pg,0,2); pg.wait_for_timeout(400); print('   Genova',pg.evaluate("()=>[AMB.birds[0].k,AMB.rain.length]")); shot(pg,oy,'f_gulls.png')
    # C16 Marseille part 2 music
    print('C16 music st3/part2 ->',pg.evaluate("()=>{ST.stage=3;ST.part=2;ST.mode='playing';ST.bossIn=false;ST.bossDead=false;return musicWant()}"))
    # C17 map tour + credits
    pg.evaluate("()=>{ST.cityScore={1:8400,2:9100,3:15200,4:7300};ST.score=40000;showMap(3,'tour')}"); pg.wait_for_timeout(600); shot(pg,oy,'f_tour.png')
    pg.evaluate("()=>mapContinue()"); pg.wait_for_timeout(300); pg.evaluate("()=>mapContinue()"); m=pg.evaluate("()=>ST.mode")
    pg.wait_for_timeout(2500); shot(pg,oy,'f_cred1.png'); pg.evaluate("()=>{ST.credT=900}"); pg.wait_for_timeout(300); shot(pg,oy,'f_cred2.png')
    pg.keyboard.press('Enter'); print('C17 tour -> ',m,'| Enter ->',pg.evaluate("()=>ST.mode"))
    # A4 record shown after reload
    pg.reload(); pg.wait_for_timeout(1200); pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}")
    pg.keyboard.press('Enter'); pg.click('#cc0'); pg.click('#toStage'); pg.wait_for_timeout(200)
    print('A4 record after reload:',pg.evaluate("()=>document.getElementById('lr0').textContent"),'| settings kept',pg.evaluate("()=>[SET.mus,SET.sfx]"))
    shot(pg,oy,'f_stages.png')
    print('ERR',errs,'| console errors',cons[:3]); b.close()
