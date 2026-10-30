from playwright.sync_api import sync_playwright
from PIL import Image
import io
def start(pg,stage,ch=0):
    pg.evaluate("()=>{gTitle()}"); pg.keyboard.press('Enter'); pg.click(f'#cc{ch}'); pg.click('#toStage'); pg.click(f'#lc{stage-1}'); pg.click('#goBtn'); pg.evaluate("()=>{if(ST.mode==='map')mapStart()}"); pg.wait_for_timeout(400)
    pg.evaluate("()=>{ST.frame=400;enemies=[];obs=[];spawnT=99999;}")
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(1000)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}")
    # 1 spawn statistics (simulated 20 min of spawner calls)
    for st in (1,2,3):
        start(pg,st)
        r=pg.evaluate("""()=>{const c={bottle:0,gend:0};ST.gendNext=0;
          for(let i=0;i<1100;i++){ST.frame+=110;ST.scrollX=(i%100)/100*ST.maxScroll;enemies=enemies.filter(e=>e.type===6&&Math.random()<.5);const n=enemies.length;spawnEnemy();
            if(enemies.length>n){const e=enemies[enemies.length-1]; e.type===6?c.gend++:c.bottle++;}}
          return c;}""")
        print('stage',st,'spawns',r, 'gendarme share %.0f%%'%(100*r['gend']/max(1,r['gend']+r['bottle'])))
    start(pg,1)
    oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    strip=[]
    def snap(cx=None,w=200):
        if cx is None: cx=pg.evaluate("()=>{const e=enemies.find(e=>e.type===6);return e?e.x+e.w/2-ST.scrollX:240}")
        im=Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+250,'width':480,'height':250}))); x0=int(max(0,min(480-w,cx-w/2))); strip.append(im.crop((x0,0,x0+w,250)))
    # 2 orientation from both sides + taunt
    pg.evaluate("()=>{Math.random=(()=>{const r=Math.random;return ()=>r()})();PL.x=ST.scrollX+120;const R=Math.random;Math.random=()=>0.1;spawnGend();Math.random=R;}")
    pg.wait_for_timeout(700); d1=pg.evaluate("()=>{const e=enemies[0];return {dir:e.dir,st:e.st}}"); snap()
    pg.wait_for_timeout(500); snap()
    pg.evaluate("()=>{enemies=[];PL.x=ST.scrollX+330;const R=Math.random;Math.random=()=>0.95;spawnGend();Math.random=R;}")
    pg.wait_for_timeout(1100); d2=pg.evaluate("()=>{const e=enemies[0];return {dir:e.dir,st:e.st}}"); snap()
    print('from right ->',d1,' from left ->',d2)
    # 3 attacks vs counters (dmgTaken is the would-be energy loss)
    def attack(state,crouch,dist=50,pre=''):
        pg.evaluate(f"""()=>{{enemies=[];eshots=[];ST.dmgTaken=0;PL.x=ST.scrollX+220;PL.jy=0;PL.air=false;K.d={1 if crouch else 0};
          spawnGend();const e=enemies[0];e.x=PL.x-{dist}-e.w/2;e.dir=1;e.taunted=true;e.hp=10;gendSet(e,'{state}');e.cd=999;e.gcd=999;{pre}}}""")
    res={}
    for name,state,cr,dist in [('fendente, in piedi','wave',0,50),('fendente, abbassato','wave',1,50),('colpo dall\'alto, abbassato','down',1,50),('colpo dall\'alto, lontano','down',0,110),('balzo, fermo','leap',0,160)]:
        attack(state,cr,dist); pg.wait_for_timeout(250)
        if name in ('fendente, in piedi','balzo, fermo','colpo dall\'alto, abbassato'): snap()
        pg.wait_for_timeout(700); res[name]=pg.evaluate("()=>ST.dmgTaken")
    pg.evaluate("()=>{K.d=0}")
    attack('throw',0,260); pg.wait_for_timeout(260); snap(); pg.wait_for_timeout(1300); res['granata, fermo']=pg.evaluate("()=>ST.dmgTaken")
    print('danno previsto per attacco:',res)
    # 4 parry
    pg.evaluate("()=>{enemies=[];shots=[];spawnGend();const e=enemies[0];e.x=PL.x+140;e.dir=-1;e.taunted=true;gendSet(e,'parry');e.cd=999;e.gcd=999;PL.dir=1;PL.shootCd=0;window.__hp=e.hp;}")
    pg.keyboard.down('z'); pg.wait_for_timeout(300); snap(); pg.keyboard.up('z'); pg.wait_for_timeout(300)
    print('parry: hp before',pg.evaluate("()=>__hp"),'after',pg.evaluate("()=>enemies[0].hp"))
    # 5 death + corpse (enemy on the right, facing left)
    pg.evaluate("()=>{const e=enemies[0];gendSet(e,'walk');e.pcd=999;e.hp=1}"); pg.keyboard.down('z'); pg.wait_for_timeout(250); pg.keyboard.up('z')
    snap(); pg.wait_for_timeout(250); snap(); pg.wait_for_timeout(500)
    cor=pg.evaluate("()=>corpses.filter(c=>c.key==='gend_death2').map(c=>({flip:c.flip,x:Math.round(c.x-ST.scrollX)}))"); snap(cor[0]['x'] if cor else None)
    print('corpse',cor,'score',pg.evaluate("()=>ST.score"),'ERR',errs)
    W=200*len(strip); out=Image.new('RGB',(W,250))
    for i,s in enumerate(strip): out.paste(s,(i*200,0))
    out.crop((0,0,200*6,250)).save('gend_strip1.png'); out.crop((200*6,0,W,250)).save('gend_strip2.png')
    b.close()
