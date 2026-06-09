---
title: "納瓦爾工作坊 v2.0 · 跨機器交接包（給 Mac 上的新 Claude Code）"
date: 2026-06-09
project: navalbook
type: handoff
tags: [navalbook, 個人商品化, 工作坊, handoff, 跨機器, mac, 扛霸子]
---

# 🧳 跨機器交接包 — Mac 上的 Claude Code 從這裡接手

> **這份 = 取代 Windows 本機記憶。** Claude 的自動記憶（`~/.claude/.../memory/`）**不會**跟著機器走，所以這份把所有狀態寫死在 vault 裡（會隨 Google Drive 同步到 Mac）。
> 開新對話第一句：「讀 `00-交接包v2-Mac接手-給新Session.md` 與同夾 `00-檔案索引.md`，接續納瓦爾工作坊 v2.0。」

---

## 0. 一句話

給「**扛霸子**」（保險經紀團隊領導／處經理級）的「**納瓦爾 × 將個人商品化 × 做自己生命的設計師**」**11 分頁互動工作坊網站**，已上線。
**鐵限制**：不出現「**竹孟／築夢／修哥**」（讀書法段用本名「**孟修**」）。

## 1. 線上 ＋ 原始碼（最重要）

- **🌐 線上站（已上線）**：<https://lawsuger.github.io/naval-workshop/>
- **📦 GitHub repo（公開）**：<https://github.com/lawsuger/naval-workshop>
- **主視覺公式**：個人商品力 ＝ ［(獨特性 × 特定知識) × 當責 × 槓桿］^(時間複利 × 造運引擎)

### ⭐ Mac 上最無縫的接續方式 = 直接用 git（不必搬檔案）
```bash
# 1) 裝/登入（若還沒）
brew install gh        # 或 brew install git
gh auth login          # 選 GitHub.com / HTTPS / 用瀏覽器登入 lawsuger

# 2) clone 部署 repo（這就是線上站本體）
git clone https://github.com/lawsuger/naval-workshop.git
cd naval-workshop

# 3) 用 Claude Code 打開這個資料夾，編輯 index.html …

# 4) 改完推上去 = 自動重新部署（約 1 分鐘生效）
git add -A && git commit -m "你的修改說明" && git push
```
> repo 內容＝自足的線上站：`index.html`（主站）＋`opening/`（去品牌動畫）＋`webapp/`（互動工作簿）。
> **編輯主站 = 改 `index.html`**。改完 push 即上線。

### 另一條路：直接編 vault 母檔（會 Google Drive 同步）
- vault 母檔（與線上 `index.html` **同內容**）：`大腦資料庫/outputs/readings/2026-06-08-…處經理工作坊/2026-06-09-工作坊完整網站.html`
- 改完母檔 → 複製成 repo 的 `index.html` → push。（或直接編 repo 的 index.html，再把改動同步回母檔，保持兩邊一致。）

## 2. vault 在 Mac 哪裡

vault（`大腦資料庫`）在 **Google Drive 同步資料夾**內：
- Windows：`F:\google雲端資料夾\Obsidian-Vaults\大腦資料庫\`
- **Mac**：你的 Google Drive 掛載點下的**同一相對路徑** `…/google雲端資料夾/Obsidian-Vaults/大腦資料庫/`
  （Mac 的 Google Drive 通常在 `~/Library/CloudStorage/GoogleDrive-lawsuger@gmail.com/我的雲端硬碟/` 之類；用 Finder 找到 `大腦資料庫` 即可）
- 本專案資料夾：vault 內 `outputs/readings/2026-06-08-納瓦爾讀書會-個人商品化-生命設計師-處經理工作坊/`
- **全部檔案清單**見同夾 `00-檔案索引.md`。

## 3. 11 分頁的網站結構（都在 `index.html` 一個檔）

| 分頁 | 內容 | 關鍵 JS |
|---|---|---|
| 首頁 | 英雄區（書本字級標題）＋中文公式一整條＋路線圖 | `show()` 切換分頁 |
| ① 39 金句 | 39 卡**點開 modal**（中英＋④書庫＋⑤名人，7 分類）＋那瓦爾生平＋寶典＋**扛霸子金句牆**(Vol-01) | `D[]`、`openQ()` |
| ② 孟修 WIKI 大腦 | 嵌**去品牌動畫** `opening/…孟修…html`＋四工具六步驟 | iframe |
| ③ 為什麼工作坊 | 5 理由（教就是最好的學習…） | — |
| ④ 造運引擎 | Λ＝L₀+(U×C×K)×R＋五階層＋四階段＋三種人30年＋破冰遊戲＋**22 題測驗** | `QZ[]`、`startQuiz()`、`submitQuiz()` |
| ⑤ 將自己商品化 | 六模組卡**點開看學員痛點**(showPain)＋互動工作簿＋保險三痛點留白 | `PAIN{}`、`showPain()` |
| ⑥ 顧問團 | 結業（信物＋誓言）＋**AI 顧問團 iframe** | `ADVISOR{}`、`renderAdvisor()` |
| 🔥21天挑戰 / ⏳時間槓桿 / 📚圖書館(23本) / 📋使用手冊 | checklist(localStorage 存) / 37.78× 矩陣 / `LIB[]` / checklist | — |

## 4. 要改特定東西，改哪裡（`index.html` 內）

- **換 AI 顧問團網址**：原始碼最上方 `const ADVISOR = { url: "…" }` 改一行（目前＝`https://thinker-advisory-panel.onrender.com`「思想家顧問團·語音數位人」）。空字串＝顯示佔位卡。`embedHTML` 可貼嵌入碼（優先於 url）。
- **改 39 金句**：JS `const D=[…]`（每條 {n,t,en,zh,site,chen,lib,web}）。
- **改 22 題測驗**：JS `const QZ=[…]`（{f:'A/B/C/D', t:'題目'}）；計分在 `submitQuiz()`（A機會察覺=U / B直覺=C / C自我實現=K / D韌性=R，每構面 0-100、總分平均）。原始題庫：`C:\Users\User\luck-engine-web\content\quiz-22.ts`（Mac 上若沒這專案，題目已內建在 index.html）。
- **改學員痛點/金句牆**：JS `const PAIN={…}`＋第一部金句牆 HTML；資料母檔 `2026-06-09-Vol01課前問卷痛點分析-納瓦爾對應.md`＋`2026-06-09-Vol01學員金句牆.md`。
- **改圖書館 23 本**：JS `const LIB=[…]`（{c:分類, ic, t, au, ds, res:[[標籤,網址]]}）。
- **配色/字體**：`<style>` 最上方 `:root` 變數（那瓦爾藍金 `--bg:#082743` / `--gold:#E9B627`；中文 Noto Serif TC 700 / Noto Sans TC；英文 Playfair Display）。

## 5. 三版同步 ＋ 簡報（在 vault，不在 git repo）

- **MD 完整內容**：`2026-06-09-工作坊網站-完整內容.md`（三版母本）
- **PPTX 簡報 22 張**：`slides-v2/納瓦爾工作坊-簡報.pptx`；產生器 `slides-v2/build_pptx.py`
  → Mac 重生：`uv run --with python-pptx python build_pptx.py`（需 uv；設計字體要裝 Noto Serif/Sans TC＋Playfair Display 才顯示）
- **簡報設計 Prompt**（貼 Gamma/Gemini 產同款）：`slides-v2/PROMPT-簡報設計-給其他AI或工具.md`
- **線上 QR**：`slides-v2/QR-工作坊網站.png`；重生 `slides-v2/make_qr.py`（`uv run --with "qrcode[pil]" python make_qr.py`）

## 6. 現況：已完成

✅ 11 分頁站上線 ✅ 39 金句 modal ✅ 去品牌動畫 ✅ 5 理由 ✅ 造運引擎簡化＋22 題測驗 ✅ 學員痛點互動＋金句牆 ✅ AI 顧問團已嵌（思想家顧問團）✅ 四件練功器 ✅ MD＋PPTX＋設計 Prompt＋QR ✅ 全程零 console error、扛霸子受眾、無竹孟/築夢/修哥。

## 7. 待辦 / 注意

1. **PPTX 設計字體**：Mac 要裝 Noto Serif TC、Noto Sans TC、Playfair Display（免費 Google Fonts），PowerPoint/Keynote 才顯示成設計樣子。
2. **顧問團是 Render 免費版**：閒置會休眠，**工作坊當天開場前先開一次** <https://thinker-advisory-panel.onrender.com> 喚醒（約十幾秒）。
3. **模組五保險三痛點**（增員難／市場飽和／帶人管理）＝**扛霸子親填、AI 不代寫**（班規），index.html 內已留虛線佔位。
4. 舊資產（海報 poster/、紙本 print/、舊 slides/、開場 MP4、配樂版）也都在本專案資料夾，需要再用。

## 8. 跨機器/環境的坑（省你踩雷）

- **git 推送看起來像錯誤其實正常**：`git push` 的「To https://github.com…」在某些終端會被當 stderr 顯示，看到 `* [new branch]` / `..main -> main` 就是成功。
- **部署 repo 有平行 session 的工作**：commit `5bc94dc`（Vol-01 金句牆＋學員痛點）非單一 session 所做。改部署站前先 `git log` / `git pull`，別用舊版覆蓋。
- Windows 端曾用 PowerShell `Get-Content -match '中文'` 誤判（cp950）；Mac 沒這問題（UTF-8）。

## 9. 底座素材（要深挖時）

- 39 金句母檔：`naval-lab/2026-06-08-naval-htgr39/`（桌面亦有 `納瓦爾39條-互動對照.html`）
- 造運引擎：`naval-lab/syntheses/07-luck-engine-productize-merged.html`、`15-section3-luck-engine-module.md`、`LuckEngine_Vault/`
- 那瓦爾生平講稿：`naval-lab/_xiu-tasks/luck-engine-input/開場稿-Naval介紹.md`
- 工作坊總手冊（六模組逐段）：`00-工作坊總手冊-處經理個人使用說明書.md`

---

> v2.0（2026-06-09）。打包檔：同夾 `納瓦爾工作坊-v2-完整打包-2026-06-09.zip`（含本交接包＋index＋動畫＋工作簿＋MD＋slides-v2＋Vol-01 資料）。
> 但**最無縫**的接續是 §1 的 `git clone`——repo 即線上站，改完 push 就更新。
