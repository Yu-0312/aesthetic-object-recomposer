# Aesthetic Object Recomposer

將普通物件照片重組為適合社群發布的生活風格攝影，並以**不改變構圖的三階段流程**產出 Editorial、Kawaii Clean 與 Kawaii Story。最新版以 **Hero Story** 為食物、飲料、桌面與共享餐點的預設文字故事路徑，強調一眼可讀的主標與活潑的角色敘事。

[English README](README.en.md)

## 輸出版本

| 階段 | 目的 | 視覺規則 |
| --- | --- | --- |
| **Editorial** | 將來源物件整理為自然、有窗光感的生活風格攝影。 | 保留物件種類、數量、材質、比例、標籤與辨識特徵。 |
| **Kawaii Clean** | 以 Editorial 為不可變底圖，加上精簡的 Q 版角色。 | 僅加入表情、短手腳與少量動態符號，不改變攝影場景。 |
| **Kawaii Story — Hero Story** | 對活潑社群情境建立具辨識度的故事畫面。 | 以一個白色手寫主標、1–2 個短反應文案、有機白線雲朵與暖色手繪節奏推進情緒。 |
| **Kawaii Story — Light Story** | 用於明確要求極簡、安靜或高級感的情境。 | 保留相同照片與角色，只使用低密度、小型註解。 |

## Hero Story v2 完整推進圖

每張最新版範例固定呈現 **Original → Editorial → Kawaii → Kawaii Story**。前三格鎖定鏡位、裁切、物件位置、光線、陰影與景深；第四格則以 Hero Story 強化可讀性、情緒與社群敘事。

### 飲料與筆電

![Drink and laptop Hero Story v2 progression](examples/drink-laptop-comparison-v2.png)

### 雙杯

![Two cups Hero Story v2 progression](examples/two-cups-comparison-v2.png)

### 火鍋餐桌

![Hotpot Hero Story v2 progression](examples/hotpot-comparison-v2.png)

### 牛排早餐

![Breakfast Hero Story v2 progression](examples/breakfast-comparison-v2.png)

### 共享餐桌

![Shared meal Hero Story v2 progression](examples/shared-meal-comparison-v2.png)

### 塔可炸物

![Taco feast Hero Story v2 progression](examples/taco-comparison-v2.png)

## 使用方式

將 skill 資料夾複製到 Codex skills 目錄後，重新開啟 Codex，即可透過 `$aesthetic-object-recomposer` 使用。

```bash
cp -R skill/aesthetic-object-recomposer ~/.codex/skills/
```

## 選擇輸出版本

原始照片視為第 1 版輸入。開始生成前，skill 會先詢問你要哪一個輸出版本；如果你沒有明確選擇，它不會直接開始生成。

| 你的選擇 | 會交付的圖片 | 系統內部處理 |
| --- | --- | --- |
| **第 2 版**／Editorial | 乾淨的重組攝影成品 | 原始圖 → 第 2 版 |
| **第 3 版**／Kawaii Clean | 只有 Q 版角色覆蓋的圖片 | 會先建立第 2 版作為底圖，但只交付第 3 版 |
| **第 4 版**／Kawaii Story | 有 Hero Story 或 Light Story 文字敘事的圖片 | 會先建立第 2、3 版作為底圖，但只交付第 4 版 |
| **指定組合**，例如 2 + 4 | 只交付你指定的版本 | 必要的中間底圖會在內部建立 |
| **完整 2–4 推進組** | 第 2、3、4 版 | 依序建立並交付全部三個版本 |

可以直接說「只要第 3 版」、「做第 4 版 Hero Story」、「輸出 2 + 4」，或「做完整推進組」。若你還需要一張 Original → Editorial → Kawaii → Kawaii Story 的四格比較圖，請另外指定「要比較圖」。除非使用者明確要求最小化處理，食物、飲料、桌面與共享餐點的第 4 版預設採用 Hero Story。

## Hero Story 準則

Hero Story 的主標應位於上方或其他乾淨留白，使用粗圓、白色手寫字與細深色描邊；必要時以貼近文字輪廓的透明白線雲朵提高可讀性。小型反應文字需以細箭頭、尾巴或動態線連向角色。裝飾維持非均勻群集，並只使用白色與一至兩種從照片擷取的暖色或主色。所有覆蓋元素必須避開產品標籤、食物紋理、人物臉部、手部與重要高光。

## 檔案結構

```text
.
├── README.md
├── README.en.md
├── aesthetic-object-recomposer.zip
├── examples/
│   ├── drink-laptop-comparison-v2.png
│   ├── two-cups-comparison-v2.png
│   ├── hotpot-comparison-v2.png
│   ├── breakfast-comparison-v2.png
│   ├── shared-meal-comparison-v2.png
│   └── taco-comparison-v2.png
└── skill/
    └── aesthetic-object-recomposer/
        ├── SKILL.md
        └── references/
            └── kawaii-story-hero.md
```

## 注意事項

Kawaii Story 是對已核准 Kawaii Clean 圖的 overlay pass；不得移動、替換、重繪或新增照片中的實體物件。小型文字與商標的準確性仍取決於所使用的圖像模型，若需精確中文，應採用可控的後製排字流程。

## License

Skill 文件與程式碼採用 [MIT License](LICENSE)。範例圖片的使用權仍屬各自原始權利人。
