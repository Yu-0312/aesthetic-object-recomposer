# Kawaii Story Captioning

Create version C as a caption-only pass over the approved Kawaii Clean image.

## Content hierarchy

Use 1–3 caption groups:

1. **Hero voice:** the main object's emotion, action, or complaint.
2. **Supporting reaction:** a short response from one supporting object.
3. **Scene note:** an optional tiny mood or action label.

Examples:

- `今天也要加油！`
- `先吃一口～`
- `太香了吧！`
- `我準備好了`
- `等等我！`
- `好酥脆！`

Do not copy text from reference images. Write original captions that fit the supplied subject.

## Length and density

- Chinese: 4–12 characters per group.
- English: 1–5 words per group.
- Use no more than 3 caption groups or 28 Chinese characters total.
- Keep total text coverage below 16% of the frame.
- Prefer one larger hero caption and one or two smaller reactions.

## Placement

- Place text in calm negative space adjacent to its speaking object.
- Connect captions with a short speech tail, curved arrow, or dotted motion path.
- Maintain at least 4% canvas padding from all edges.
- Never cover labels, food texture, faces, hands, utensils, controls, or major highlights.
- Avoid placing text across mixed high-contrast backgrounds.

## Typography

- Use lively hand-drawn scrapbook lettering with irregular baselines, playful rotation, and visibly varied character size.
- Build a clear hierarchy: one bold comic-style hero phrase, one smaller handwritten reaction, and an optional tiny scene note.
- Use cream or white as the reading base, plus 2–4 source-derived accent colors for key words, punctuation, stars, music notes, and emphasis marks.
- Add a thick contrasting outline or sticker-like border so every phrase remains readable over photography.
- Mix filled bubble lettering, loose handwritten notes, and compact speech balloons while keeping the set visually coherent.
- Short English exclamations such as `WOW!`, `YUM!`, `GO!`, or `HI!` may be combined with exact Chinese copy when they strengthen the character action.
- Allow rounded speech bubbles, burst shapes, thought clouds, curved arrows, dotted paths, sparkles, blush marks, and motion lines.
- Avoid rigid typesetting, corporate fonts, dense rectangular text boxes, long paragraphs, or perfectly aligned captions.

## Reference-energy target

- Match the cheerful social-post energy of kawaii food doodle references: expressive faces first, playful captions second, decorative marks third.
- Captions should feel physically connected to the speaking object through a tail, arrow, pose, or nearby action mark.
- Favor asymmetry and rhythm: one large phrase, one medium reaction, several tiny marks—not three identical labels.
- Keep overlays handmade and spontaneous, but make all Chinese glyphs deterministic and exact.

## Story-prop illustration

- Start with emotional shorthand: blush, sweat drop, question mark, surprise rays, sleepy `Z`, sparkle, heart, music note, or a tiny motion trail. These are preferred over literal props.
- When the scene supports it, add 1–2 small illustrated props that turn the caption into an action: chef hat, spoon, fork, flag, headband, instrument, menu, alarm clock, shopping bag, or tiny costume accessory.
- Attach a prop lightly to an existing character or place a separate mini illustration in adjacent negative space. Never paste a large colored shape across the photographed subject.
- Match the existing doodle line weight, outline color, blush palette, lighting mood, and simplified perspective. Favor airy outline drawing with only 1–2 small color fills sampled from the photo.
- Keep all new illustration coverage around 3–6% of the frame, with an absolute maximum of 8%, and never hide the photographed object's identifying surface, label, face, or food texture.
- Do not add a full new photographed object. Story props are clearly hand-drawn overlays only.

## Integration test

- At thumbnail size, the photograph must read first and the new illustration second.
- The overlay should feel removable without leaving a compositional hole; it supports the image but does not become the hero.
- Reject oversized hats, utensils, badges, solid geometric stickers, or captions that sit on top of the food.

## Accuracy strategy

- For short decorative English, model-rendered lettering is acceptable after visual verification.
- For Chinese or exact copy, prefer deterministic post-production typesetting when available.
- If model-rendered text contains any wrong glyph, remove it and typeset the exact supplied text locally.
- Never ship approximate Chinese, invented characters, or unreadable pseudo-writing.

## Quality gate

- Every caption is exact, legible, and clearly associated with one object.
- Text adds personality or story rather than describing the obvious.
- The approved Kawaii Clean image is otherwise unchanged.
- The frame still reads first as a photograph, second as a character scene, and third as a captioned story.
