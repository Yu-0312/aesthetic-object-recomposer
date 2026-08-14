# Aesthetic Object Recomposer

Recompose ordinary object photos into social-ready editorial lifestyle imagery, then produce matched **Editorial**, **Kawaii Clean**, and **Kawaii Story** stages without composition drift. The current version defaults food, drinks, desktops, and shared meals to **Hero Story**, a bolder storytelling route built around immediate headline readability and playful character interaction.

[中文 README](README.md)

## Output modes

| Stage | Purpose | Visual rule |
| --- | --- | --- |
| **Editorial** | Arrange the source objects into calm, natural lifestyle photography. | Preserve object type, count, material, proportion, label, and identity-defining details. |
| **Kawaii Clean** | Add controlled kawaii characters over an immutable Editorial base. | Add only faces, short limbs, and sparse motion marks; do not alter the photograph. |
| **Kawaii Story — Hero Story** | Create an expressive social storytelling image for lively subjects. | Use one bold white handwritten headline, 1–2 short reactions, an organic white-outline cloud, and warm hand-drawn accent rhythm. |
| **Kawaii Story — Light Story** | Serve explicitly minimal, quiet, or premium requests. | Preserve the same photo and character layer, adding only low-density small annotations. |

## Hero Story v2 progression boards

Every current example presents **Original → Editorial → Kawaii → Kawaii Story**. The first three panels lock camera, crop, placement, lighting, shadows, and depth of field. The fourth panel uses Hero Story to strengthen readability, emotion, and social storytelling.

### Drink + Laptop

![Drink and laptop Hero Story v2 progression](examples/drink-laptop-comparison-v2.png)

### Two Cups

![Two cups Hero Story v2 progression](examples/two-cups-comparison-v2.png)

### Hotpot Table

![Hotpot Hero Story v2 progression](examples/hotpot-comparison-v2.png)

### Steak Breakfast

![Breakfast Hero Story v2 progression](examples/breakfast-comparison-v2.png)

### Shared Meal

![Shared meal Hero Story v2 progression](examples/shared-meal-comparison-v2.png)

### Taco Feast

![Taco feast Hero Story v2 progression](examples/taco-comparison-v2.png)

## Installation and use

Copy the skill directory to the Codex skills directory, restart Codex, and invoke `$aesthetic-object-recomposer`.

```bash
cp -R skill/aesthetic-object-recomposer ~/.codex/skills/
```

## Select an output version

Treat the original photo as Version 1 input. Before generating, the skill asks which output you want; it does not begin generation until a version is chosen.

| Your selection | Delivered image | Internal processing |
| --- | --- | --- |
| **Version 2** / Editorial | Clean recomposed lifestyle photograph | Original → V2 |
| **Version 3** / Kawaii Clean | Character-overlay image only | Builds V2 as the base, then delivers V3 only |
| **Version 4** / Kawaii Story | Hero Story or Light Story captioned image only | Builds V2 and V3 as bases, then delivers V4 only |
| **Selected combination**, such as 2 + 4 | Only the named versions | Builds required intermediate bases internally |
| **Full V2–V4 progression** | V2, V3, and V4 | Builds and delivers all three stages |

You can say “Version 3 only,” “make Version 4 Hero Story,” “output 2 + 4,” or “make the full progression.” If you also need a four-panel Original → Editorial → Kawaii → Kawaii Story board, explicitly ask for a comparison board. Unless a minimal treatment is explicitly requested, Version 4 defaults to Hero Story for food, drinks, desktops, and shared meals.

## Hero Story direction

Place the primary headline in upper or otherwise calm negative space. Use bold, rounded white handwritten lettering with a thin dark keyline; when contrast requires it, use an organic transparent white-outline cloud that follows the words closely. Connect each short reaction to its character with a small arrow, tail, or motion mark. Cluster decorations asymmetrically and limit color to white plus one or two source-derived warm or dominant accents. Never cover product labels, food texture, faces, hands, or important highlights.

## File layout

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

## Notes

Kawaii Story is an overlay pass over an approved Kawaii Clean image. It must not move, replace, repaint, or invent photographed objects. The accuracy of small labels and characters still depends on the selected image model; use controllable post-production typesetting when exact Chinese text is required.

## License

Skill documentation and code are released under the [MIT License](LICENSE). Example-image rights remain with their respective owners.
