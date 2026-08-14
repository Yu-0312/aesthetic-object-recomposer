---
name: aesthetic-object-recomposer
description: Recompose objects from an uploaded photo into polished editorial, kawaii-clean, or kawaii-story images while preserving object identity. Use when Codex should rearrange food, drinks, cameras, books, tableware, furniture, decor, or products into deliberate editorial compositions, and let the user choose version 2 (Editorial), version 3 (Kawaii Clean), version 4 (Kawaii Story), selected combinations, or the complete 2–4 progression.
---

# Aesthetic Object Recomposer

Create the finished image whenever an image-editing or image-generation tool is available. Do not return only a prompt unless image generation is unavailable or the user explicitly asks for a prompt.

## Output Selection Gate — run before image work

Treat the uploaded source photo as **Version 1 — Original**. It is input only and must never be regenerated. Before analysing or generating images, determine which output versions the user wants.

| User selection | Generate | Required source chain | Deliver |
| --- | --- | --- | --- |
| **2** / Editorial / photography | **Version 2 — Editorial** | Original → V2 | V2 only |
| **3** / Kawaii / Kawaii Clean | **Version 3 — Kawaii Clean** | Original → V2 → V3, unless an approved V2 is supplied | V3 only |
| **4** / Kawaii Story / Story | **Version 4 — Kawaii Story** | Original → V2 → V3 → V4, unless an approved V3 is supplied | V4 only |
| **2 + 3**, **3 + 4**, or another explicit set | Every selected version | Build omitted prerequisites silently when necessary | Only the selected versions |
| **2–4** / complete set / full progression | V2, V3, and V4 | Original → V2 → V3 → V4 | V2, V3, and V4; make a 1–4 comparison board only if requested |

Apply these gate rules:

1. Ask one concise question and wait **before generating** when the user has not selected a version: `要生成第 2 版 Editorial、第 3 版 Kawaii Clean、第 4 版 Kawaii Story，還是完整 2–4 推進組？`
2. Infer a selection only when the request is unambiguous. Treat `只要可愛版` as V3, `只要故事字版` as V4, and `整組／比較圖` as V2–V4.
3. For V4, default to **Hero Story** for playful food, drinks, desktops, and shared meals. Use **Light Story** only when the user requests minimal, premium, quiet, or unobtrusive annotation.
4. Create hidden prerequisites only to protect geometry. Do not return V2 or V3 when the user selected V4 only, unless they ask to review the progression.
5. Start directly from an attached or clearly identified approved V2 for V3, or approved V3 for V4. Otherwise, build the full dependency chain; never create V3 from the original or V4 from anything other than V3.
6. Confirm whether a comparison board is requested separately from the version selection. A board always includes Original → Editorial → Kawaii Clean → Kawaii Story.

## Workflow

1. Run the **Output Selection Gate**.
2. Inspect the source photo and create an object inventory: hero object, supporting objects, vessels, surfaces, furniture, readable labels, and identity-defining details.
3. Lock invariants before redesigning: object count, category, silhouette, materials, dominant colors, logos, labels, food type, and distinctive wear or garnish.
4. Choose a recomposition strength:
   - **Light:** preserve the location and camera angle; improve spacing, crop, and light.
   - **Standard:** preserve objects but rebuild their arrangement and camera framing.
   - **Scene rebuild:** preserve objects while placing them in a new warm editorial interior. Use only when the user requests a new scene or the source background is unusable.
5. Select one composition from [composition-system.md](references/composition-system.md). Do not mix several diagrams without a clear dominant structure.
6. Apply the photographic direction in [visual-language.md](references/visual-language.md), then read [kawaii-routing.md](references/kawaii-routing.md) whenever V3 or V4 is selected.
7. Before creating V4, read [text-captioning.md](references/text-captioning.md). Also read [kawaii-story-hero.md](references/kawaii-story-hero.md) whenever Hero Story is selected. Compile all edit requests using [prompt-recipes.md](references/prompt-recipes.md).
8. Generate V2 from the original, V3 by editing approved V2, and V4 by editing approved V3. Build only the chain needed for the selected endpoint. Default to portrait 4:5; use 9:16 for stories and 1:1 for square posts.
9. Evaluate object fidelity, physical plausibility, composition, lighting, depth, stage consistency, illustration integration, caption accuracy, and unwanted additions. Make one targeted correction if a major check fails.
10. Deliver only the selected output versions. Name outputs clearly as `editorial`, `kawaii-clean`, and `kawaii-story`; use `comparison-board` only when explicitly requested.

## Dependency lock

- V2, V3, and V4 must share the same canvas, crop, camera angle, lens perspective, object positions, scale, overlap, lighting, shadows, background, color grade, and depth of field whenever more than one stage is created.
- V3 may add only faces, short limbs, tiny props, motion marks, sparkles, and very short decorative lettering.
- V4 may add only planned white handwritten captions, transparent white-outline speech bubbles, arrows, lively emotion marks, and 1–2 small story-supporting illustrations placed beside or lightly attached to existing characters. In Hero Story, allow one dominant headline and deliberately clustered small marks; in Light Story, keep captions sparse and small.
- V3 and V4 must not move, resize, replace, duplicate, remove, or restyle any photographed object.
- Use approved V2 as V3's source and approved V3 as V4's source. When a later version is selected alone, create its prerequisites silently unless a clearly approved base image is supplied.

## Staging Rules

- Establish one unmistakable hero object.
- Use 1–3 supporting objects unless the source clearly contains a larger set.
- Group objects in odd numbers when possible while respecting the source count.
- Vary height, scale, and rotation. Avoid equal spacing and perfectly parallel objects.
- Allow controlled overlap of roughly 5–15% to create depth; never hide the hero's identifying feature.
- Ground every object with contact shadow, weight, and correct perspective. Nothing may float.
- Leave 20–45% calm negative space unless the user requests a dense tabletop spread.
- Use foreground, subject plane, and soft background to create three-layer depth.
- Remove clutter only when it is not part of the protected inventory.
- Do not show composition grids, dotted guides, labels, or explanatory text in the final image. The reference diagrams are planning tools only.
- In V3, use sparse hand-drawn overlays. In V4, choose the route first: default to **Hero Story** for playful food, drink, desktop, and group-meal scenes, using one bold headline, 1–3 short reactions, and clustered white/scene-colored marks at roughly 10–18% coverage; use **Light Story** only for explicit minimal or premium requests, keeping overlay around 3–8%. In both routes, keep the photograph dominant, use white hand-drawn lettering and transparent white bubble outlines, never use cream label cards or colored UI-like caption boxes, and never cover product labels, food texture, faces, hands, controls, or hero silhouettes.

## Fidelity Guardrails

- Do not replace a specific camera, cup, plate, dessert, book, chair, or product with a generic substitute.
- Do not invent extra food, utensils, flowers, candles, books, furniture, labels, people, hands, or brand marks unless the user requests them.
- Preserve exact visible text when feasible. If exact text cannot be guaranteed, keep the original label region visually faithful instead of creating fake words.
- Preserve food freshness, realistic scale, and correct serving ware.
- Preserve optical and mechanical details on cameras and products; do not add impossible controls or duplicate lenses.
- Keep shadows consistent with a single primary window-light direction.

## Quality Gate

Accept only when all major checks pass:

- Every protected object is present exactly once and immediately recognizable.
- One dominant composition clearly organizes the frame.
- The hero reads within one second at thumbnail size.
- Objects have plausible scale, perspective, overlap, contact, and shadows.
- Warm editorial styling supports the objects rather than overpowering them.
- Background blur is optical and gradual, not a cutout halo.
- Highlights retain texture on glass, ceramics, food, paper, and wood.
- No grid, annotation, watermark, social-media UI, gibberish text, or unexpected object appears.
- When V3 or V4 is selected, the face, limbs, and props feel attached to the intended object and the photograph remains dominant.
- When V4 is selected, captions are readable and intentional, with no gibberish, accidental text, or subject obstruction. In Hero Story, one dominant headline creates immediate thumbnail impact; in Light Story, restraint is intentional rather than a loss of energy.
- When more than one stage is generated, all stages align perfectly when overlaid; only the intended doodles and captions differ.

Correct only the failed dimension. Do not replace a successful arrangement wholesale.
