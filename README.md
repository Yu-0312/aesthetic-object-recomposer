# Aesthetic Object Recomposer

把普通照片中的食物、飲料、產品與桌面物件，重新排列成適合 Instagram 的生活風格攝影，並額外產出相同構圖的 Q 版角色塗鴉版本。

[English README](README.en.md)

## 核心特色

- 保留原物件的種類、數量、材質、顏色、標籤與辨識特徵。
- 支援對角線、三角形、S 型、L 型、桌角、置中、三分法與留白構圖。
- 預設輸出一組相互配對的圖片：
  1. **Editorial**：乾淨、自然、具有窗光與雜誌感的網美攝影版。
  2. **Kawaii**：直接在 Editorial 成品上加入 Q 版表情、短手腳與少量塗鴉。
- Q 版階段鎖定裁切、鏡位、物件位置、光線、陰影與景深，避免兩張圖構圖漂移。
- 自動避免假文字、浮空物件、重複餐點、過度橘色、HDR 與社群介面。

## 安裝

將 Skill 資料夾複製到 Codex skills 目錄：

```bash
cp -R skill/aesthetic-object-recomposer ~/.codex/skills/
```

也可以下載並解壓縮根目錄的 [`aesthetic-object-recomposer.zip`](aesthetic-object-recomposer.zip)。

重新開啟 Codex 後，即可透過 `$aesthetic-object-recomposer` 使用。

## 使用範例

```text
使用 $aesthetic-object-recomposer，把這張照片中的物體重新排成網美照，
並輸出一張相同構圖的 Q 版。
```

```text
保留飲料杯、標籤與吸管，改成暖木桌、自然窗光的對角構圖。
第二張讓兩個杯子變成互相打招呼的可愛角色。
```

## 工作流程

1. 分析原圖並建立物件清單。
2. 鎖定不可改變的物件特徵。
3. 選擇適合的構圖與重排強度。
4. 先生成乾淨的 Editorial 版本。
5. 以 Editorial 圖片為底圖，只加入 Q 版 overlay。
6. 檢查物件完整性、接觸陰影、景深與兩張圖片的一致性。

## 前後對比

每張圖依序為：**原圖 → 網美重排版 → Q 版**。

### 飲料與筆電

![Drink and laptop comparison](examples/drink-laptop-comparison.png)

### 雙杯

![Two cups comparison](examples/two-cups-comparison.png)

### 火鍋餐桌

![Hotpot comparison](examples/hotpot-comparison.png)

### 牛排早餐

![Breakfast comparison](examples/breakfast-comparison.png)

### 共享餐桌

![Shared meal comparison](examples/shared-meal-comparison.png)

### 塔可炸物

![Taco comparison](examples/taco-comparison.png)

### 雙碗拉麵

![Ramen comparison](examples/ramen-comparison.png)

### 咖哩飯

![Curry comparison](examples/curry-comparison.png)

### 火腿蛋早餐

![Ham and egg breakfast comparison](examples/ham-breakfast-comparison.png)

## 檔案結構

```text
.
├── README.md
├── README.en.md
├── aesthetic-object-recomposer.zip
├── examples/
└── skill/
    └── aesthetic-object-recomposer/
        ├── SKILL.md
        ├── agents/openai.yaml
        └── references/
```

## 注意事項

- 圖像生成模型仍可能無法百分之百重現非常細小的文字或商標。
- Q 版圖層應保持稀疏，不應遮住食品質感或產品標籤。
- 如果原圖包含人物，預設不在人物臉部加塗鴉。
- 範例圖片僅用於展示 Skill 的圖像轉換流程。

## License

Skill 文件與程式碼採用 [MIT License](LICENSE)。範例圖片的使用權仍屬各自原始權利人。
