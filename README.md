# 飲料設計師實驗室 🧃

高中彈性學習課程（2 × 50 分鐘）：**用數學調出一杯完美飲料**。
以 2026 年發表於英國皇家化學會期刊的機能性飲料配方最佳化論文為素材，讓學生扮演「一日飲料設計師」——先討論、再揭曉，拉滑桿調配方，最後用 Excel / Python / R 自己算出最佳解。

🔗 **線上使用**：<https://tai-shengyeh.github.io/beverage-lab/>

## 課程內容

| 單元 | 內容 | 互動形式 |
|------|------|----------|
| 單元 1 | 有超能力的飲料（機能性飲料的定義與市場） | 討論 → 揭曉 |
| 單元 2 | 食品的身分證（pH、°Brix、黏度、密度、水活性、總多酚） | 討論 → 揭曉 |
| 實驗室 A | 果汁調配模擬器（蘋果 × 葡萄 × 蔓越莓） | 滑桿 + 三角圖 + 即時判定 |
| 單元 3 | 配方的科學：理論派 TMO vs 實驗派 DoE | 猜測 → 揭曉 + 全班投票 |
| 實驗室 B | 植物奶蛋白質挑戰（米 × 豌豆 × 杏仁） | 滑桿 + 四項限制達標挑戰 |
| 程式角落 | 用 Excel 規劃求解 / Python scipy / R 網格搜尋找最佳配方 | 三選一動手算 |
| 結業測驗 | 10 題單選即時計分，可上傳成績給老師 | 測驗 + 雲端回收 |

模擬器的計算引擎使用論文中經實驗驗證的迴歸模型（式 6、9、10 與 Table 6、8、S3），不是隨意編造的數字。

## 檔案說明

- `index.html` — 完整課程頁（單一檔案，含所有互動功能，可離線使用）
- `juice_lab.py` — 果汁配方最佳化 Python 版（scipy 約束最佳化，適用 Google Colab）
- `juice_lab.R` — 果汁配方最佳化 R 版（網格搜尋法，適用 Posit Cloud）

## 使用方式

直接用瀏覽器開啟 `index.html`（或點上方線上連結）即可上課，無需安裝、手機／平板／桌機皆可。

- 🖥 **投影模式**：右上角按鈕一鍵放大字級並強制淺色，適合教室投影機
- 🌓 自動跟隨系統深／淺色主題
- 網址加上 `?projector=1` 可直接以投影模式開啟

### 給老師

- 「討論 → 揭曉」閘門：先讓學生分組討論，按下按鈕才顯示科學家的答案
- 盲測預測投票與測驗成績會上傳到 Firebase（離線或連線失敗時自動靜默停用，不影響其他功能）；成績只收班級座號與分數，不收姓名
- 程式角落的三個工具（Excel 規劃求解／Python／R）擇一即可，Excel 版與論文作者使用的工具相同

## 技術

純前端：HTML + CSS + 原生 JavaScript，單一檔案、無建置流程。雲端互動（投票統計、成績回收）使用 Firebase Firestore，以動態 `import` 載入、失敗時完全不影響頁面其他功能。

## 教材來源與授權

Navarrete-González, R., López-Malo, A., Palou, E., & Ramírez-Corona, N. (2026).
A comparative study of theoretical model-based optimization and experimental design approaches for functional beverage formulation.
*Sustainable Food Technology*, 4, 947–960. DOI: [10.1039/d5fb00480b](https://doi.org/10.1039/d5fb00480b)（CC-BY 4.0）

模擬器所用之迴歸係數取自該論文；模型輸出為估計值，僅供教學。

—

© 葉泰聖（Tai-Sheng Yeh）· [食品科學教學課程](https://tai-shengyeh.github.io/)
