# Automated full runs: every character through every city (god mode), looking for stuck states and errors
from playwright.sync_api import sync_playwright
import time,sys
BOT="""(arg)=>{ const [c,s,god,pt]=arg;
  PROG.tut=true; selChar=c; ST.char=c; ST.stage=s; ST.score=0; ST.lives=99; ST.startPart=1; ST.rush=null;
  MAP={from:null,to:s,t:0,fire:false}; ST.startPart=pt||1; mapStart(); setGod(god);
  let f=0, lastX=-1, lastProg=0, lockT=0, maxLock=0, notes=[], parts=[ST.part];
  const t0=performance.now();
  while(f<90000){
    f++;
    const boss=enemies.find(e=>e.type===5&&e.hp>0);
    let tg=null,bd=1e9; for(const e of enemies){ if(e.hp<=0||e.type===5) continue; const ex=e.x+e.w/2; if(ex<ST.scrollX-10||ex>ST.scrollX+W+10) continue; const d=Math.abs(ex-PL.x); if(d<bd){bd=d;tg=e;} }
    if(tg&&ST.lockCam){ const dx=tg.x+tg.w/2-PL.x; K.r=dx>0?1:0; K.l=dx<0?1:0; if(Math.abs(dx)<50&&f%3) { K.r=K.l=0; PL.dir=dx>0?1:-1; } }
    else if(tg&&bd<120&&tg.x+tg.w/2<PL.x&&f%40<20){ K.r=0; K.l=0; PL.dir=-1; }      // turn to hit what's behind, but keep advancing
    else { K.r=boss?(Math.floor(f/150)%3!==0?1:0):1; K.l=boss&&!K.r?1:0; }
    K.s=1; K.d=(tg&&tg.type===7&&bd<120)?1:0;
    const danger=eshots.some(b=>Math.abs(b.x-PL.x)<110&&b.y>GROUND-110)||enemies.some(e=>e.hp>0&&(e.type===6||e.type===7)&&Math.abs(e.x+e.w/2-PL.x)<70);
    if((danger&&f%12===0)||f%140===0) jumpQ=true;
    if(f%420===0) doBomb();
    try{ update(); }catch(e){ notes.push('EXC '+e.message+' @'+f); break; }
    if(ST.mode==='win'){ break; }
    if(ST.mode==='gameover'){ notes.push('gameover @'+f); break; }
    if(ST.part!==parts[parts.length-1]){ parts.push(ST.part); lastX=-1; lastProg=f; }
    if(ST.scrollX>lastX+1){ lastX=ST.scrollX; lastProg=f; }
    if(ST.lockCam&&!ST.bossIn) { lockT++; maxLock=Math.max(maxLock,lockT); } else lockT=0;
    if(f-lastProg>3600&&!ST.bossIn&&!ST.partT){ notes.push('STUCK scroll='+Math.round(ST.scrollX)+' lock='+ST.lockCam+' wave='+!!ST.wave+' trev='+ST.trevFight+' en='+JSON.stringify(enemies.map(e=>[e.type,Math.round(e.x-ST.scrollX),e.hp,e.wave?1:0,e.st||'',Math.round(e.y),e.h]))+' obs='+JSON.stringify(obs.filter(o=>o.hp>0&&o.x>ST.scrollX-50&&o.x<ST.scrollX+W).map(o=>[o.type,Math.round(o.x-ST.scrollX),o.hp,o.h]))+' pl='+Math.round(PL.x-ST.scrollX)+' dir='+PL.dir+' shots='+shots.length+' melee='+PL.melee+' vx='+PL.vx+' K='+JSON.stringify(K)+' air='+PL.air+' stun='+PL.stunT+' hurt='+PL.hurtT+' chute='+PL.chute+' land='+PL.landT+' pick='+PL.pickT+' bomb='+PL.bombT); break; }
    if(ST.bossIn&&boss===undefined&&!ST.bossDead&&f-lastProg>6000){ notes.push('boss missing'); break; }
  }
  return {ev:ST.ev&&ST.ev.k,evDone:ST.ev&&ST.ev.done,gendK:ST.gendK,eliteK:ST.eliteK,bossTime:ST.bossTime&&Math.round(ST.bossTime),specs:ST.spec&&ST.spec.got.length,c,s,mode:ST.mode,frames:f,secs:Math.round(f/60),parts,score:ST.score,kills:ST.kills,dmg:ST.dmgTaken,maxLockS:Math.round(maxLock/60),notes,ms:Math.round(performance.now()-t0)};
}"""
god=(sys.argv[1]!='nogod') if len(sys.argv)>1 else True
with sync_playwright() as p:
    b=p.chromium.launch(); res=[]
    for c in range(5):
        for s,pt in ((2,2),(2,3)):
            pg=b.new_page(viewport={'width':480,'height':700}); errs=[]; pg.on('pageerror',lambda e,errs=errs:errs.append(str(e)))
            pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(700)
            r=pg.evaluate(BOT,[c,s,god,pt]); r['err']=errs[:3]; print(r,flush=True); res.append(r); pg.close()
    b.close()
