# -*- coding: utf-8 -*-
"""
納瓦爾工作坊 — 完整版 HTML 投影片生成器
從 slides-master.md 解析（單一來源），輸出可翻頁、自帶樣式的單檔 HTML。
跑法： python3 build_html.py
操作：← → / 空白鍵翻頁、F 全螢幕、O 總覽、數字跳頁。
"""
import os, re, html, json

TABS={
 'home':'首頁','p1':'PART I · 39 金句','p2':'PART II · 孟修 WIKI 大腦',
 'p3':'PART III · 為什麼工作坊','p4':'PART IV · 造運引擎','p5':'PART V · 將自己商品化',
 'p6':'PART VI · 顧問團','c21':'🔥 21 天挑戰','tl':'⏳ 時間槓桿','lib':'📚 圖書館','man':'📋 使用手冊',
}

def parse(path):
    slides=[]; cur=None
    for raw in open(path,encoding='utf-8'):
        ln=raw.rstrip('\n')
        m=re.match(r'^## \[([a-z0-9]+)-(\d+)\]\s*(.+)$',ln)
        if m:
            if cur: slides.append(cur)
            cur={'tab':m.group(1),'idx':int(m.group(2)),'title':m.group(3).strip(),'point':'','body':[]}
        elif cur is not None:
            mp=re.match(r'^\*\*重點\*\*：(.+)$',ln)
            if mp: cur['point']=mp.group(1).strip()
            elif ln.startswith('- '): cur['body'].append(ln[2:].strip())
    if cur: slides.append(cur)
    return slides

def esc(s): return html.escape(s)

def render(sld,n,total):
    tab=TABS.get(sld['tab'],'')
    cover='封面' in sld['title']
    cls='slide cover' if cover else 'slide'
    title=sld['title']
    if cover: title=re.sub(r'^封面：?','',title).strip()
    parts=[f'<section class="{cls}" data-tab="{esc(sld["tab"])}">']
    parts.append(f'<div class="kick">{esc(tab)}</div>')
    parts.append(f'<h2>{esc(title)}</h2>')
    if sld['point']:
        parts.append(f'<div class="point"><span class="pl">重點</span>{esc(sld["point"])}</div>')
    if sld['body']:
        parts.append('<ul>'+''.join(f'<li>{esc(b)}</li>' for b in sld['body'])+'</ul>')
    parts.append(f'<div class="pg">{str(n).zfill(3)} / {total}　·　納瓦爾工作坊 · 給扛霸子的致富之道</div>')
    parts.append('</section>')
    return ''.join(parts)

HERE=os.path.dirname(os.path.abspath(__file__))
slides=parse(os.path.join(HERE,'slides-master.md'))
total=len(slides)
body=''.join(render(s,i+1,total) for i,s in enumerate(slides))
# 總覽用的目錄（分頁分組）
toc=[{'n':i+1,'tab':s['tab'],'title':s['title']} for i,s in enumerate(slides)]

TPL='''<!DOCTYPE html>
<html lang="zh-Hant"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>納瓦爾工作坊 · 完整版投影片</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,500&family=Noto+Serif+TC:wght@500;700;900&family=Noto+Sans+TC:wght@300;400;500;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#082743;--card:#0c3258;--inset:#06243f;--gold:#E9B627;--golds:#f4d76a;--goldd:#b98a16;--ink:#fff;--muted:#aebccb;--faint:#7e93a8;--line:#1f4a78;--serif:"Noto Serif TC",serif;--sans:"Noto Sans TC",sans-serif;--play:"Playfair Display",serif}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%}
body{background:#04111f;color:var(--ink);font-family:var(--sans);overflow:hidden}
#deck{position:fixed;inset:0;display:flex;align-items:center;justify-content:center}
.slide{display:none;width:100vw;height:100vh;max-width:1280px;max-height:720px;background:var(--bg);
  background-image:radial-gradient(900px 520px at 80% -5%,rgba(233,182,39,.13),transparent 60%),radial-gradient(760px 560px at 0% 110%,rgba(233,182,39,.07),transparent 55%);
  border-radius:6px;padding:54px 64px;flex-direction:column;position:relative;box-shadow:0 30px 90px rgba(0,0,0,.6)}
.slide.on{display:flex;animation:fade .35s ease}
@keyframes fade{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
.kick{font-family:var(--play);font-weight:700;color:var(--gold);letter-spacing:1px;font-size:15px;margin-bottom:6px;flex:0 0 auto}
.kick::before{content:"";display:inline-block;width:34px;height:5px;background:var(--gold);border-radius:3px;vertical-align:middle;margin-right:12px}
.slide h2{font-family:var(--serif);font-weight:700;color:#fff;font-size:30px;line-height:1.32;margin-bottom:14px;flex:0 0 auto}
.point{background:var(--inset);border:1px solid var(--goldd);border-radius:12px;padding:13px 18px;color:var(--golds);font-family:var(--serif);font-weight:700;font-size:18px;line-height:1.4;margin-bottom:16px;flex:0 0 auto}
.point .pl{font-family:var(--play);font-size:12px;color:var(--goldd);font-weight:700;letter-spacing:1px;margin-right:12px;vertical-align:1px}
.slide ul{list-style:none;overflow:auto;flex:1 1 auto}
.slide li{position:relative;padding-left:22px;margin:9px 0;color:var(--ink);font-size:18px;line-height:1.55;font-weight:300}
.slide li::before{content:"▸";position:absolute;left:0;color:var(--goldd)}
.slide.cover{align-items:center;justify-content:center;text-align:center}
.slide.cover .kick{margin-bottom:14px}
.slide.cover .kick::before{display:none}
.slide.cover h2{font-size:48px;color:var(--golds)}
.slide.cover .point{font-size:22px;color:var(--gold);border:none;background:transparent;text-align:center}
.slide.cover ul{flex:0 0 auto;text-align:center;color:var(--muted)}
.slide.cover li{padding-left:0;font-size:15px}.slide.cover li::before{display:none}
.pg{position:absolute;left:64px;right:64px;bottom:22px;color:var(--faint);font-size:12px;font-family:var(--play);flex:0 0 auto}
.slide.cover .pg{text-align:center;left:0;right:0}
#bar{position:fixed;left:0;top:0;height:3px;background:linear-gradient(90deg,var(--golds),var(--gold));z-index:30;transition:width .25s}
#hud{position:fixed;right:16px;bottom:14px;z-index:30;display:flex;gap:8px;align-items:center}
#hud button{background:rgba(12,50,88,.85);border:1px solid var(--line);color:var(--golds);border-radius:9px;width:40px;height:40px;font-size:18px;cursor:pointer;font-family:var(--sans)}
#hud button:hover{border-color:var(--gold)}
#hud .ctr{color:var(--faint);font-size:13px;font-family:var(--play);min-width:74px;text-align:center}
#ov{position:fixed;inset:0;background:rgba(4,17,31,.97);z-index:40;display:none;overflow:auto;padding:30px}
#ov.on{display:block}
#ov h3{color:var(--gold);font-family:var(--serif);margin:18px 0 8px;font-size:16px;border-bottom:1px solid var(--line);padding-bottom:6px}
#ov .gi{display:flex;flex-wrap:wrap;gap:7px}
#ov .gi a{background:var(--card);border:1px solid var(--line);color:var(--muted);border-radius:8px;padding:7px 11px;font-size:12.5px;cursor:pointer;max-width:340px;text-overflow:ellipsis;overflow:hidden;white-space:nowrap}
#ov .gi a:hover{border-color:var(--gold);color:var(--golds)}
#ov .n{color:var(--goldd);font-family:var(--play);margin-right:6px}
.hint{position:fixed;left:16px;bottom:14px;color:var(--faint);font-size:11.5px;z-index:30}
@media(max-width:760px){.slide{padding:30px 26px}.slide h2{font-size:22px}.slide li{font-size:15px}.point{font-size:15px}.slide.cover h2{font-size:30px}}
</style></head><body>
<div id="bar"></div>
<div id="deck">__BODY__</div>
<div id="ov"></div>
<div class="hint">← → / 空白翻頁　·　O 總覽　·　F 全螢幕</div>
<div id="hud"><button onclick="go(cur-1)">‹</button><span class="ctr" id="ctr"></span><button onclick="go(cur+1)">›</button><button onclick="toggleOv()" title="總覽">▦</button></div>
<script>
var S=[].slice.call(document.querySelectorAll('.slide'));
var TOC=__TOC__;
var cur=0, total=S.length;
function go(i){i=Math.max(0,Math.min(total-1,i));S[cur].classList.remove('on');cur=i;S[cur].classList.add('on');
  document.getElementById('bar').style.width=((cur+1)/total*100)+'%';
  document.getElementById('ctr').textContent=(cur+1)+' / '+total;
  if(location.hash!=='#'+(cur+1))history.replaceState(null,'','#'+(cur+1));}
function toggleOv(){var o=document.getElementById('ov');o.classList.toggle('on');}
function buildOv(){var o=document.getElementById('ov');var TAB={home:'首頁',p1:'PART I · 39 金句',p2:'PART II · 孟修 WIKI',p3:'PART III · 為什麼工作坊',p4:'PART IV · 造運引擎',p5:'PART V · 將自己商品化',p6:'PART VI · 顧問團',c21:'🔥 21 天挑戰',tl:'⏳ 時間槓桿',lib:'📚 圖書館',man:'📋 使用手冊'};
  var order=['home','p1','p2','p3','p4','p5','p6','c21','tl','lib','man'],h='';
  order.forEach(function(t){var items=TOC.filter(function(x){return x.tab===t});if(!items.length)return;
    h+='<h3>'+TAB[t]+'</h3><div class="gi">';
    items.forEach(function(x){h+='<a onclick="go('+(x.n-1)+');toggleOv()"><span class="n">'+String(x.n).padStart(3,'0')+'</span>'+x.title.replace(/</g,'&lt;')+'</a>'});
    h+='</div>';});
  o.innerHTML=h;}
document.addEventListener('keydown',function(e){
  if(e.key==='ArrowRight'||e.key===' '||e.key==='PageDown'){go(cur+1);e.preventDefault();}
  else if(e.key==='ArrowLeft'||e.key==='PageUp'){go(cur-1);}
  else if(e.key==='Home'){go(0);}else if(e.key==='End'){go(total-1);}
  else if(e.key==='o'||e.key==='O'){toggleOv();}
  else if(e.key==='f'||e.key==='F'){if(!document.fullscreenElement)document.documentElement.requestFullscreen();else document.exitFullscreen();}
});
buildOv();
var h=parseInt((location.hash||'#1').slice(1))-1; go(isNaN(h)?0:h);
</script></body></html>'''

out_html=TPL.replace('__BODY__',body).replace('__TOC__',json.dumps(toc,ensure_ascii=False))
out=os.path.join(HERE,'納瓦爾工作坊-完整版-投影片.html')
open(out,'w',encoding='utf-8').write(out_html)
print("OK ->",out,"| slides:",total,"| bytes:",len(out_html))
