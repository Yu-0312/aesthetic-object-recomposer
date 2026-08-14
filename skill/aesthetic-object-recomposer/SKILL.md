---
name: aesthetic-object-recomposer
description: Recompose objects from an uploaded photo into polished, Instagram-ready editorial lifestyle images while preserving each object's identity. Use when Codex should rearrange food, drinks, cameras, books, tableware, furniture, decor, or products into deliberate editorial compositions; by default deliver a matched three-image set consisting of a clean photographic version, a kawaii doodle-character version, and a kawaii storytelling version with expressive Hero Story or restrained Light Story captions, dialogue, arrows, and annotations.
---

# Aesthetic Object Recomposer

Create the finished image whenever an image-editing or image-generation tool is available. Do not return only a prompt unless image generation is unavailable or the user explicitly asks for a prompt.

## Workflow

1. Inspect the source photo and create an object inventory: hero object, supporting objects, vessels, surfaces, furniture, readable labels, and identity-defining details.
2. Lock invariants before redesigning: object count, category, silhouette, materials, dominant colors, logos, labels, food type, and distinctive wear or garnish.
3. Choose a recomposition strength:
   - **Light:** preserve the location and camera angle; improve spacing, crop, and light.
   - **Standard:** preserve objects but rebuild their arrangement and camera framing.
   - **Scene rebuild:** preserve objects while placing them in a new warm editorial interior. Use only when the user requests a new scene or the source background is unusable.
4. Select one composition from [composition-system.md](references/composition-system.md). Do not mix several diagrams without a clear dominant structure.
5. Default to a **matched three-image set** unless the user explicitly requests fewer versions:
   - **A — Photographic Editorial:** the finished clean Instagram-ready recomposition.
   - **B — Kawaii Clean:** the exact same recomposed scene with controlled Q版 characters and minimal symbols.
   - **C — Kawaii Story:** version B plus captions, dialogue, arrows, and handwritten annotations. Default to **Hero Story** for playful food, drink, desktop, and shared-meal scenes; use **Light Story** only when the user explicitly asks for minimal, premium, restrained, or unobtrusive annotations.
6. Apply the photographic direction in [visual-language.md](references/visual-language.md), then read [kawaii-routing.md](references/kawaii-routing.md) for the second-pass illustration treatment.
7. Before creating version C, read [text-captioning.md](references/text-captioning.md). Also read [kawaii-story-hero.md](references/kawaii-story-hero.md) whenever Hero Story is selected. Compile all edit requests using [prompt-recipes.md](references/prompt-recipes.md).
8. Generate A first, B by editing A, then C by editing B. Never regenerate later versions from the original. Default to portrait 4:5; use 9:16 for stories and 1:1 for square posts.
9. Evaluate object fidelity, physical plausibility, composition, lighting, depth, set consistency, illustration integration, caption accuracy, and unwanted additions. Make one targeted correction if a major check fails.

## Matched-set lock

- A, B, and C must share the same canvas, crop, camera angle, lens perspective, object positions, scale, overlap, lighting, shadows, background, color grade, and depth of field.
- B may add only faces, short limbs, tiny props, motion marks, sparkles, and very short decorative lettering.
- C may add only planned white handwritten captions, transparent white-outline speech bubbles, arrows, lively emotion marks, and 1–2 small story-supporting illustrations placed beside or lightly attached to existing characters. In Hero Story, allow one dominant headline and deliberately clustered small marks; in Light Story, keep captions sparse and small.
- B and C must not move, resize, replace, duplicate, remove, or restyle any photographed object.
- Use approved A as B's source and approved B as C's source.
- Name outputs clearly as `editorial`, `kawaii-clean`, and `kawaii-story`.

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
- In Kawaii Clean mode, use sparse hand-drawn overlays. In Kawaii Story mode, choose the route first: default to **Hero Story** for playful food, drink, desktop, and group-meal scenes, using one bold headline, 1–3 short reactions, and clustered white/scene-colored marks at roughly 10–18% coverage; use **Light Story** only for explicit minimal or premium requests, keeping overlay around 3–8%. In both routes, keep the photograph dominant, use white hand-drawn lettering and transparent white bubble outlines, never use cream label cards or colored UI-like caption boxes, and never cover product labels, food texture, faces, hands, controls, or hero silhouettes.

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
- When Kawaii mode is selected, the face, limbs, and props feel attached to the intended object and the photograph remains dominant.
- Version C uses readable, intentional captions with no gibberish, accidental text, or subject obstruction.
- In Hero Story, one dominant headline creates immediate thumbnail impact while smaller reactions and marks support a clear reading hierarchy; in Light Story, restraint is intentional rather than a loss of energy.
- Version C's extra illustrations improve balance or storytelling without becoming generic stickers or competing with the photographed hero.
- All three images align perfectly when overlaid; only the intended doodles and captions differ.

Correct only the failed dimension. Do not replace a successful arrangement wholesale.
