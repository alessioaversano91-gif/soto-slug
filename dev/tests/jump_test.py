from playwright.sync_api import sync_playwright
from PIL import Image
import io
def start(pg,ci):
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.evaluate("()=>{document.body.classList.remove('kb');fit()}"); pg.wait_for_timeout(100); pg.wait_for_timeout(900)
    pg.keyboard.press('Enter');pg.click(f'#cc{ci}');pg.click('#toStage');pg.click('#lc0');pg.click('#goBtn'); pg.evaluate("()=>{if(ST.mode==='map')mapStart()}")
    pg.evaluate("()=>{ST.frame=400;spawnEnemy=()=>{};enemies=[];}");pg.wait_for_timeout(200)
def trace(pg,ms): 
    pg.evaluate("()=>{window.__tr=[];const f=()=>{__tr.push(Math.round(PL.jy));if(__tr.length<400)requestAnimationFrame(f)};f();}")
    pg.wait_for_timeout(ms); return pg.evaluate("()=>__tr")
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':560,'height':900});errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    start(pg,0)
    # 1 fast tap (down/up in the same tick)
    pg.evaluate("()=>{document.dispatchEvent(new KeyboardEvent('keydown',{key:'x'}));document.dispatchEvent(new KeyboardEvent('keyup',{key:'x'}));}")
    tr=trace(pg,1000); print('1 tap: peak',-min(tr),'landed',tr[-1]==0)
    # 2 hold jump for 2s with OS auto-repeat events
    pg.evaluate("()=>{document.dispatchEvent(new KeyboardEvent('keydown',{key:'ArrowUp'}));window.__rep=setInterval(()=>document.dispatchEvent(new KeyboardEvent('keydown',{key:'ArrowUp',repeat:true})),33);}")
    tr=trace(pg,2000); pg.evaluate("()=>{clearInterval(__rep);document.dispatchEvent(new KeyboardEvent('keyup',{key:'ArrowUp'}))}")
    jumps=sum(1 for i in range(len(tr)) if tr[i]<0 and (i==0 or tr[i-1]==0)); print('2 hold 2s: jumps',jumps,'(expect 1)')
    # 3 jump then hold down mid-air
    pg.keyboard.press('x'); pg.wait_for_timeout(150); pg.keyboard.down('ArrowDown')
    st=pg.evaluate("()=>({air:PL.air,crouch:PL.crouch})"); pg.wait_for_timeout(900)
    st2=pg.evaluate("()=>({air:PL.air,crouch:PL.crouch,jy:PL.jy,h:PL.crouch})"); pg.keyboard.up('ArrowDown')
    print('3 down mid-air:',st,'-> after landing',st2)
    # 4 crouched jump attempt
    pg.keyboard.down('ArrowDown');pg.wait_for_timeout(100);pg.keyboard.press('x');pg.wait_for_timeout(200)
    print('4 jump while crouched: air',pg.evaluate("()=>PL.air"));pg.keyboard.up('ArrowDown')
    # 5 run + jump + fire, screenshot sequence
    frames=[]
    pg.keyboard.down('ArrowRight');pg.wait_for_timeout(300);x0=pg.evaluate("()=>PL.x");pg.keyboard.press('x')
    for i in range(5):
        pg.wait_for_timeout(120);xx=pg.evaluate("()=>PL.x-ST.scrollX")
        if i==2: pg.keyboard.down('z')
        im=Image.open(io.BytesIO(pg.screenshot(clip={'x':40,'y':150,'width':480,'height':440})))
        frames.append(im.crop((max(0,int(xx*1.07)-90),0,max(0,int(xx*1.07)-90)+180,440)))
    pg.keyboard.up('z');pg.wait_for_timeout(700);pg.keyboard.up('ArrowRight');x1=pg.evaluate("()=>PL.x")
    print('5 run-jump distance',round(x1-x0),'shots',pg.evaluate("()=>shots.length"))
    # 6 touch/pointer button
    bb=pg.locator('#jumpBtn').bounding_box();pg.mouse.move(bb['x']+20,bb['y']+20);pg.mouse.down();pg.mouse.up()
    tr=trace(pg,1000);print('6 deck button: peak',-min(tr))
    # 7 ten rapid taps
    peaks=0
    for i in range(10):
        pg.keyboard.press('x');pg.wait_for_timeout(900)
        if pg.evaluate("()=>PL.jy")==0: peaks+=1
    print('7 ten taps, all landed:',peaks==10)
    out=Image.new('RGB',(180*len(frames),440))
    for i,f in enumerate(frames): out.paste(f,(i*180,0))
    out.save('jump_seq.png')
    # 8 Seba: no jump, button hidden
    start(pg,1);pg.keyboard.press('x');pg.wait_for_timeout(300)
    print('8 Seba air:',pg.evaluate("()=>PL.air"),'button display:',pg.evaluate("()=>getComputedStyle(document.getElementById('jumpBtn')).display"))
    print('ERRORS',errs);b.close()
