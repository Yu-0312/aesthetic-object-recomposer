# Aesthetic Object Recomposer

Turn ordinary photos of food, drinks, products, and tabletop objects into polished Instagram-ready editorial images, then create a matched kawaii doodle version using the exact same composition.

[中文 README](README.md)

## Highlights

- Preserves object identity, count, materials, colors, labels, and recognizable details.
- Supports diagonal, triangle, S-curve, L-shape, table-corner, centered, rule-of-thirds, and negative-space compositions.
- Produces a matched pair by default:
  1. **Editorial:** clean lifestyle photography with natural window light and magazine styling.
  2. **Kawaii:** an overlay-only Q-style character treatment based directly on the Editorial result.
- Locks crop, camera, placement, lighting, shadows, background, and depth of field between paired images.
- Guards against fake text, floating objects, duplicate food, excessive orange grading, HDR, watermarks, and social-media UI.

## Installation

```bash
cp -R skill/aesthetic-object-recomposer ~/.codex/skills/
```

Alternatively, download and extract [`aesthetic-object-recomposer.zip`](aesthetic-object-recomposer.zip).

Restart Codex and invoke `$aesthetic-object-recomposer`.

## Example prompt

```text
Use $aesthetic-object-recomposer to rearrange the objects in this photo into an
editorial lifestyle composition, then create a matched kawaii doodle version.
```

## Workflow

1. Analyze the source and build a protected object inventory.
2. Lock identity-defining invariants.
3. Select recomposition strength and one dominant composition.
4. Generate the clean Editorial image first.
5. Use the approved Editorial image as the immutable base for the Kawaii overlay.
6. Validate object fidelity, grounding, shadows, depth, and pair consistency.

## Comparisons

Each example shows **Original → Editorial → Kawaii**.

![Drink and laptop](examples/drink-laptop-comparison.png)
![Two cups](examples/two-cups-comparison.png)
![Hotpot](examples/hotpot-comparison.png)
![Breakfast](examples/breakfast-comparison.png)
![Shared meal](examples/shared-meal-comparison.png)
![Taco feast](examples/taco-comparison.png)
![Ramen night](examples/ramen-comparison.png)
![Curry rice](examples/curry-comparison.png)
![Ham and egg breakfast](examples/ham-breakfast-comparison.png)

## Notes

- Very small labels and trademarks may not be reproduced perfectly by image models.
- Kawaii overlays should remain sparse and must not obscure food texture or product labels.
- People are not doodled by default.
- Example images are included only to demonstrate the transformation workflow.

## License

Skill documentation and code are released under the [MIT License](LICENSE). Example-image rights remain with their respective owners.
