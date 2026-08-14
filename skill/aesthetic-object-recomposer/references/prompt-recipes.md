# Prompt Recipes

Build prompts in this order: edit intent, protected inventory, composition, environment, light, camera, finish, exclusions.

## Output selection gate

1. Map **V2** to Editorial, **V3** to Kawaii Clean, and **V4** to Kawaii Story. If the user does not name a version, ask whether they want V2, V3, V4, selected combinations, or the full V2–V4 progression before generating.
2. If the user selects V2 only, generate the photographic recipe and deliver V2 only.
3. If the user selects V3 only, generate V2 silently from the original unless an approved V2 is supplied; then use that V2 as the immutable source for V3 and deliver V3 only.
4. If the user selects V4 only, generate V2 and V3 silently unless an approved V3 is supplied; then use that V3 as the immutable source for V4 and deliver V4 only.
5. For a selected combination, deliver only the named versions. For a full V2–V4 progression, deliver all three. Make an Original → V2 → V3 → V4 comparison board only when the user separately requests a board.

## Dependency workflow

1. Generate **V2 — Editorial** with one of the photographic recipes below.
2. Confirm that the objects, composition, lighting, and crop pass the quality gate.
3. Use V2 as the input image for **V3 — Kawaii Clean** with the overlay-only recipe below when V3 or V4 is needed.
4. Use V3 as the input image for **V4 — Kawaii Story** when V4 is needed. Default to the Hero Story recipe for playful social scenes; use the Light Story recipe only for an explicitly minimal or premium treatment.
5. Compare stages by overlay or rapid alternation whenever more than one stage is created. Outside illustrated and caption pixels, the scene must remain visually identical.

## Standard recomposition

> Edit the supplied image into a polished vertical 4:5 editorial lifestyle photograph. Preserve exactly these objects and their identity: [INVENTORY]. Reposition the objects into a clear [COMPOSITION] arrangement with one hero, controlled overlap, varied height, natural spacing, and 20–45% calm negative space. Keep all objects physically grounded with correct perspective and contact shadows. Use a warm wood tabletop, restrained café interior, one directional window-light source, soft geometric sunlight, natural 35–50 mm perspective, and gradual optical depth of field. Apply warm brown, cream, muted olive, soft gray, and source-derived accent colors with gentle filmic contrast and fine grain. Preserve exact materials, silhouettes, proportions, logos, labels, food type, garnish, and object count. No extra props, duplicate objects, people, hands, floating items, fake text, watermark, social-media UI, composition grid, annotation, heavy HDR, orange cast, or excessive blur.

## Light recomposition

> Improve only the arrangement, crop, spacing, and lighting of the supplied photo. Preserve the existing location, camera angle, every protected object, background architecture, and object identity. Organize the frame around [COMPOSITION], strengthen one hero, create subtle foreground-to-background depth, and use one believable window-light direction. Do not replace objects or rebuild the room. No additions, removals, duplicate items, fake labels, watermark, grid, or text overlay.

## Scene rebuild

> Rebuild the scene around the supplied objects while preserving each protected object exactly: [INVENTORY]. Arrange them in a [COMPOSITION] on a warm walnut or teak surface near a sunlit window in a quiet independent café or design-studio interior. Add only structural background elements needed for depth: one wooden chair, one softly blurred window, and a calm plaster wall. Keep the source objects identical in count, silhouette, materials, colors, logos, labels, and details. Natural late-morning window light, long soft-edged shadows, 50 mm editorial photography, f/3.5 equivalent depth, tactile wood and paper, restrained filmic warmth. No decorative clutter, flowers, candles, extra books, extra tableware, people, hands, duplicate products, fake branding, watermark, composition guides, or text overlay.

## Kawaii doodle character route

> Edit the supplied photo into a polished vertical 4:5 social lifestyle image. Preserve exactly these photographed objects and their identity: [INVENTORY]. Recompose them into a clear [COMPOSITION] with realistic perspective, contact shadows, warm window light, tactile wood or fabric, and gradual photographic depth. Keep the photograph fully realistic. Add sparse original kawaii hand-drawn overlays only to the selected hero objects: simple dot or curved eyes, one small expressive mouth, soft blush, and at most two short arms and legs attached to believable silhouette edges. Give each character one readable action or emotion: [ACTION]. Add only a few white motion lines, sparkles, music notes, curved arrows, or a tiny speech bubble; illustration coverage below 18% of the frame. Use source-derived accent colors and white outlines. Preserve all food texture, package design, logos, labels, colors, materials, object count, and proportions. No full-cartoon conversion, copyrighted characters, extra products, dense writing, long generated captions, detached limbs, extra faces, fake labels, watermark, social-media UI, composition grid, or tutorial annotation.

## Kawaii overlay-only second pass

> Use the supplied approved editorial image as an immutable photographic base. Do not change the canvas, crop, camera, perspective, object placement, size, rotation, overlap, background, lighting, shadow, color grade, texture, focus, or depth of field. Add sparse original Q版 hand-drawn overlays only to [SELECTED OBJECTS]: simple expressive eyes, one small mouth, optional blush, and at most two short arms and legs attached to believable silhouette edges. Show [ACTION/EMOTION] with a few white or source-colored motion lines, sparkles, musical notes, tiny props, or one very short decorative word. Keep illustration coverage below 18% of the frame and below 25% of each object. Preserve every label, logo, control, food texture, material, and silhouette. This is an overlay edit, not a regeneration. No object movement, replacement, duplication, removal, full-cartoon conversion, copyrighted character, dense handwriting, fake label, watermark, UI, grid, or tutorial annotation.

## Kawaii Hero Story third pass

> Use the supplied approved Kawaii Clean image as an immutable base. Preserve every photographic pixel and all existing character faces, limbs, props, and symbols. Build a lively kawaii social-post story layer without changing the photo. Reserve clean upper-third negative space for one large exact Chinese headline: [HERO HEADLINE]. Render it in bold rounded white hand-drawn lettering with a slim dark-brown or charcoal keyline and soft light shadow. Place it at roughly 20–30% of canvas width. Enclose it with one transparent irregular white-outline cloud only when the background needs separation; the cloud must follow the lettering organically and never look like a filled card. Add [SUPPORTING CAPTION 1] near [ANCHOR 1] and [SUPPORTING CAPTION 2] near [ANCHOR 2] in smaller white handwritten lettering, connected with delicate curved pointers. Add a deliberate asymmetric rhythm of [MARKS]: white stars, hearts, steam curls, focus rays, lightning, music notes, blush, sweat drops, tiny flags, or motion strokes, with at most two source-derived accent colors. Give the selected existing kawaii characters a clear emotional link to the words, but do not change their faces or add new characters. Keep overall new text-and-mark coverage around 10–18% and never above 22%; keep props below 8%. Preserve labels, food texture, faces, hands, controls, hero silhouettes, and major highlights. Render every requested caption exactly as supplied. No moved objects, changed lighting, new photographed props, cream cards, colored caption fills, pill badges, generic fonts, dense paragraphs, watermark, social-media UI, composition grid, or tutorial diagram.

## Kawaii Light Story third pass

> Use the supplied approved Kawaii Clean image as an immutable base. Preserve every photographic pixel and all existing character faces, limbs, props, and symbols. Add only the planned storytelling layer: [CAPTION 1] near [ANCHOR 1], [CAPTION 2] near [ANCHOR 2], and optionally [CAPTION 3] near [ANCHOR 3]. Render captions in white hand-drawn lettering with a thin dark keyline. Enclose selected phrases with small transparent irregular white-outline speech bubbles or hand-drawn circles; do not use cream cards, colored caption fills, pill badges, or UI-like boxes. Add only a few white curved arrows, sparkles, music notes, and emotion marks. Keep total added overlay below 8% and place text only in calm negative space; never cover food texture, product labels, faces, hands, controls, or hero silhouettes. Render all requested text exactly as supplied. No new photographed objects, new characters, changed expressions, moved doodles, oversized props, dense paragraphs, fake labels, watermark, social-media UI, composition grid, or tutorial diagram.

## Targeted corrections

- Object drift: `Restore the exact source object design, count, materials, colors, labels, and proportions; change only placement and scene styling.`
- Floating objects: `Add physically correct table contact, perspective, and soft contact shadows beneath every object.`
- Weak hero: `Increase the hero's scale by 12%, sharpen it selectively, and reduce the support objects' contrast.`
- Too staged: `Introduce small natural rotations and spacing variations; remove two nonessential props.`
- Too orange: `Neutralize whites and highlights; keep warmth in wood and sunlight rather than applying an orange color wash.`
- Fake blur: `Replace cutout blur with gradual optical depth of field and preserve clean subject edges.`
- Busy frame: `Remove all invented props and restore 35% calm negative space.`
- Excess doodles: `Remove half the illustration marks; keep one face and one action per intended hero while restoring clear product and food texture.`
- Awkward character anatomy: `Reattach short doodle limbs to believable silhouette edges and remove all detached or duplicate facial features.`
- Pair drift: `Restore the approved editorial base exactly and reapply only the Q版 overlay; no photographic pixel geometry, lighting, texture, or object placement may change.`
- Caption errors: `Remove every incorrect glyph and typeset the supplied captions exactly; preserve the approved Kawaii Clean image unchanged.`
- Busy Hero Story: `Keep the dominant headline, one supporting reaction, and the most meaningful decorative cluster; remove evenly scattered marks and restore unobstructed food and product details.`
- Weak Hero Story: `Enlarge the exact hero headline by 20%, place it in clean upper-third negative space, strengthen its dark keyline, and add one organic white-outline cloud only if contrast needs support.`
- Busy Light Story: `Keep only the three most meaningful captions and move them into calm negative space; restore unobstructed food and product details.`
