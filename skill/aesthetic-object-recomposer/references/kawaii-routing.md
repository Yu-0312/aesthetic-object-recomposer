# Kawaii Routing

Treat kawaii styling as two passes over an approved photographic recomposition: a clean character overlay, followed by an optional storytelling overlay with captions.

## Use Kawaii Doodle Character mode when

- The hero is rounded, soft, edible, drinkable, plush, or naturally character-like.
- The source already feels playful, colorful, casual, youthful, or snack-oriented.
- The object has a clear face zone: cup body, bun surface, fruit skin, dessert top, package front, or plush head.
- The user asks for Q版, 可愛, 萌, doodle, sticker, character, anthropomorphic, or social-story styling.
- A simple action or emotion can be communicated without changing the physical object.

Good candidates: bread, buns, fruit, smoothies, coffee cups, ice cream, noodles, packaged snacks, plush toys, cute stationery, and casual food sets.

## Prefer Photographic Editorial mode when

- The hero is architecture, furniture, camera equipment, luxury goods, minimalist industrial design, or a serious branded product.
- The source relies on material precision, calm negative space, premium mood, or documentary credibility.
- Doodles would hide labels, controls, food texture, or structural details.
- The user asks for natural, premium, minimal, cinematic, editorial, or realistic styling.

## Output decision

- Default: make A Photographic Editorial, B Kawaii Clean, and C Kawaii Story.
- If the subject is especially suitable for Q版, give B a clear action and slightly richer doodles while retaining the same photo.
- If the subject is serious or precision-led, still make B when paired output is requested or implied, but use an ultra-light treatment: one subtle face or a few reaction marks without covering controls, labels, or structure.
- Make fewer versions only when the user explicitly requests them.

## Story route decision

- Default to **Hero Story** for playful food, drinks, snack spreads, casual desktop scenes, and shared meals. It uses one bold hand-drawn headline, 1–3 short reactions, and clustered small marks for immediate social-post impact.
- Use **Light Story** only when the user asks for a minimal, premium, quiet, editorial, or unobtrusive story layer.
- If the user provides a lively kawaii-story reference with a large headline, cloud outline, expressive objects, and colorful perimeter marks, match that energy with Hero Story rather than reducing it to sparse annotations.
- Read [kawaii-story-hero.md](kawaii-story-hero.md) before composing Hero Story. Read [text-captioning.md](text-captioning.md) for exact wording and placement in both routes.

## Set-lock requirements

- Finish and approve A before creating B.
- Use A as the direct editing source for B.
- Finish and approve B before creating C; use B as C's source.
- Pixel geometry outside doodle regions should remain unchanged: identical crop, object placement, lighting, shadows, texture, background, and blur.
- Never regenerate B from scratch with merely a similar prompt.
- If B causes object drift, restore A and repeat only the overlay pass.
- If C causes object or doodle drift, restore B and repeat only the caption pass.

## Kawaii visual grammar

- Keep the source photograph, object arrangement, and realistic lighting as the base.
- Add one simple face to each intended hero character: two dot or curved eyes, one small mouth, and optional blush circles.
- Add at most two short arms and two short legs per character. Attach them to believable silhouette edges.
- In Light Story, use white hand-drawn captions, curved arrows, motion lines, sparkles, music notes, or speech bubbles sparingly. In Hero Story, use one dominant headline and intentionally clustered marks; do not scatter decorations evenly.
- Use 2–4 accent colors derived from the source plus white outlines; Hero Story should limit colored accents to one or two source-derived warm hues.
- Give each character one readable emotion or action: happy, sleepy, surprised, cooking, exercising, playing music, drinking, or celebrating.
- Keep illustration coverage below roughly 18% of the frame and below 25% of any hero object. Hero Story normally uses 10–18% of the canvas; Light Story normally uses 3–8%.
- Preserve logos and labels; place facial features around them rather than on top of them.
- Keep text short. In Hero Story, use one 4–8-character Chinese headline plus 1–3 supporting reactions of 3–7 Chinese characters. In Light Story, use small 4–12-character captions only. Avoid dense writing.
- Reserve multi-caption storytelling for version C and follow [text-captioning.md](text-captioning.md).

## Never

- Convert the entire scene into a flat cartoon unless explicitly requested.
- Add disturbing facial features, extra eyes, detached limbs, or anatomy that obscures the food or product.
- Invent copyrighted characters, recognizable mascots, or third-party stickers.
- Add dense captions, composition grids, tutorial labels, watermarks, or social-media UI.
