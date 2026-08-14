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
- Use white hand-drawn captions, curved arrows, motion lines, sparkles, music notes, or speech bubbles sparingly.
- Use 2–4 accent colors derived from the source plus white outlines.
- Give each character one readable emotion or action: happy, sleepy, surprised, cooking, exercising, playing music, drinking, or celebrating.
- Keep illustration coverage below roughly 18% of the frame and below 25% of any hero object.
- Preserve logos and labels; place facial features around them rather than on top of them.
- Keep text short. Prefer one or two words such as `HI`, `WOW`, `YUM`, `OK`, or no text. Avoid long generated handwriting.
- Reserve multi-caption storytelling for version C and follow [text-captioning.md](text-captioning.md).


## Never


- Convert the entire scene into a flat cartoon unless explicitly requested.
- Add disturbing facial features, extra eyes, detached limbs, or anatomy that obscures the food or product.
- Invent copyrighted characters, recognizable mascots, or third-party stickers.
- Add dense captions, composition grids, tutorial labels, watermarks, or social-media UI.



## Kawaii Clean v2 Routing

- Select one hero character and no more than two supporting characters from the photographed objects.
- Give each character a role: hero reacts or leads, support characters answer, assist, carry, point, or decorate. Do not give every object the same face or pose.
- Before drawing, specify for each character: face zone, emotion, action verb, limb attachment edges, one optional action prop, and one source-derived accent color.
- Use a readable three-level action scale: Level 1 expression only; Level 2 expression plus short limbs; Level 3 expression, limbs, and one prop or motion mark. Use Level 3 for the hero and Level 1–2 for supports unless the scene clearly needs more energy.
- Keep facial grammar consistent: two eyes, one mouth, optional blush, and at most one emotion cue. Keep limbs short, attached, and pointed toward the action.
- Preserve the original object silhouette, label, texture, highlight, contact shadow, and camera geometry. Keep clean-mode overlay coverage around 10–18% of the frame and below 28% of each selected object.
- Save a character continuity record before Story: character IDs, face positions, emotions, poses, limb anchors, props, accent colors, and the intended next story beat.

### Story handoff

Kawaii Story must inherit the same character IDs, faces, limbs, props, and pose logic. It may amplify the action with one large white hero phrase, one or two short reactions, arrows, burst rays, bubbles, and small side illustrations, but it must not redesign the clean characters or move the photographic objects.
