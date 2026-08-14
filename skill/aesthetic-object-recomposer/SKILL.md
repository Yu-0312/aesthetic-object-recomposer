---
name: aesthetic-object-recomposer
description: Recompose objects from an uploaded photo into polished, Instagram-ready editorial lifestyle images while preserving each object's identity. Use when Codex should rearrange food, drinks, cameras, books, tableware, furniture, decor, or products into deliberate editorial compositions; by default deliver a matched three-image set consisting of a clean photographic version, a kawaii doodle-character version, and a kawaii storytelling version with short captions, dialogue, arrows, and annotations.
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
   - **B — Kawaii Clean:** the exact same recomposed scene with a coherent Q版 character system, readable poses, expressive faces, attached limbs, and a small set of action props and motion marks.
   - **C — Kawaii Story:** version B plus short captions, dialogue, arrows, and handwritten annotations.
6. Apply the photographic direction in [visual-language.md](references/visual-language.md), then read [kawaii-routing.md](references/kawaii-routing.md) for the second-pass illustration treatment.
7. Read [text-captioning.md](references/text-captioning.md) before creating version C. Compile all edit requests using [prompt-recipes.md](references/prompt-recipes.md).
8. Generate A first, B by editing A, then C by editing B. Never regenerate later versions from the original. Default to portrait 4:5; use 9:16 for stories and 1:1 for square posts.
9. Evaluate object fidelity, physical plausibility, composition, lighting, depth, set consistency, illustration integration, caption accuracy, and unwanted additions. Make one targeted correction if a major check fails.




## Matched-set lock




- A, B, and C must share the same canvas, crop, camera angle, lens perspective, object positions, scale, overlap, lighting, shadows, background, color grade, and depth of field.
- B may add a coherent character layer to selected photographed objects: expressive faces, short attached limbs, one readable pose or action per character, one small action prop when useful, motion marks, sparkles, and at most one tiny decorative word.
- C may add a planned lively storytelling layer on top of B: one large white handwritten hero phrase, one or two short reactions, transparent white-outline speech bubbles, arrows, burst rays, lively emotion marks, and 1–2 story-supporting illustrations placed beside or lightly attached to existing characters.
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

## Kawaii Clean v2 Character Gate

- Build one unmistakable hero character and no more than two supporting characters. The hero receives the clearest face, strongest pose, and most readable action.
- Assign one action verb and one emotion to each character before drawing. The pose must read without captions.
- Use two eyes, one mouth, optional blush, and at most one extra emotion cue per character. Never duplicate facial features.
- Use at most two short arms and two short legs per character. Attach every limb to a believable silhouette edge and point it toward the action or prop.
- Add at most one small attached action prop per character. Use a consistent line weight, eye style, blush color, and source-derived accent palette.
- Keep clean-mode illustration coverage around 10–18% of the frame and below 28% of each selected object. Preserve labels, controls, food texture, highlights, hands, and the hero silhouette.
- Record the hero action, emotion, face placement, limb attachment points, prop, and accent colors before creating Kawaii Story; the fourth image must extend this character layer without redesigning it.

Correct only the failed Kawaii Clean dimension; do not regenerate the photographic composition.
