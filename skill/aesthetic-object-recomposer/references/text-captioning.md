# Kawaii Story Captioning

Create version C as a caption-only pass over the approved Kawaii Clean image. Choose **Hero Story** for lively food, drink, desktop, snack-spread, and shared-meal images; choose **Light Story** only when a minimal or premium treatment is explicitly requested. Read [kawaii-story-hero.md](kawaii-story-hero.md) for Hero Story composition and prompting.

## Content hierarchy

Use a clear three-level hierarchy.

1. **Hero Story headline:** one energetic 4–8-character Chinese exclamation that creates thumbnail impact, such as `元氣早餐！`, `充電中！`, `一起吃吧！`, or `開動啦！`.
2. **Supporting reaction:** one or two 3–7-character responses that connect a selected object to the headline.
3. **Scene note:** an optional tiny mood or action label, such as `FOCUS!`, `YUM!`, a music note, or a short handwritten aside.

For Light Story, omit the dominant headline and use one to three small caption groups instead.

Examples:

- `今天也要加油！`
- `先吃一口～`
- `太香了吧！`
- `我準備好了`
- `等等我！`
- `好酥脆！`

Do not copy text from reference images. Write original captions that fit the supplied subject.

## Length and density

- Hero Story: headline 4–8 Chinese characters; each supporting reaction 3–7 Chinese characters. Use one headline, one or two reactions, and an optional tiny scene note.
- Light Story: Chinese 4–12 characters per group; English 1–5 words per group.
- Keep the Hero Story text-and-mark overlay around 10–18% of the frame, never above 22%. Keep Light Story below 8%.
- Prefer one large hero headline, one medium reaction, and one small note. Do not use three captions of equal size.

## Placement

- Place text in calm negative space adjacent to its speaking object.
- Connect captions with a short speech tail, curved arrow, or dotted motion path.
- Maintain at least 4% canvas padding from all edges.
- Never cover labels, food texture, faces, hands, utensils, controls, or major highlights.
- Avoid placing text across mixed high-contrast backgrounds.

## Typography

- Use lively hand-drawn scrapbook lettering with irregular baselines, playful rotation, and visibly varied character size.
- In Hero Story, set the headline at roughly 20–30% of canvas width in bold, rounded comic-style lettering. Make it clearly larger than all reactions. In Light Story, keep all text secondary.
- Make white the dominant lettering and bubble color. Use thick white hand-drawn strokes with a slim dark brown or charcoal keyline and soft light shadow for contrast.
- Keep speech bubbles transparent: draw an irregular white outline around the text rather than placing text on a cream, colored, or solid rectangular sticker.
- Use source-derived accent colors mainly for nearby character illustrations and tiny punctuation—not for the main caption fill.
- Mix white bubble lettering, loose white handwritten notes, and compact white speech balloons while keeping the set visually coherent.
- Short English exclamations such as `WOW!`, `YUM!`, `GO!`, or `HI!` may be combined with exact Chinese copy when they strengthen the character action.
- Allow rounded speech bubbles, hand-drawn circles, irregular speech frames, thought clouds, curved arrows, dotted paths, sparkles, blush marks, and motion lines. Keep their outlines white.
- Avoid rigid typesetting, corporate fonts, dense rectangular text boxes, long paragraphs, or perfectly aligned captions.

## Reference-energy target

- Match the cheerful social-post energy of kawaii food doodle references: expressive faces first, playful captions second, decorative marks third.
- Captions should feel physically connected to the speaking object through a tail, arrow, pose, or nearby action mark.
- Favor asymmetry and rhythm: one large phrase, one medium reaction, several tiny marks—not three identical labels.
- Keep overlays handmade and spontaneous, but make all Chinese glyphs deterministic and exact.
- Reject cream label cards, colored caption boxes, pill-shaped UI badges, and typography that resembles an app interface.

## Story-prop illustration

- Start with emotional shorthand: blush, sweat drop, question mark, surprise rays, sleepy `Z`, sparkle, heart, music note, or a tiny motion trail. These are preferred over literal props.
- When the scene supports it, add 1–2 small illustrated props that turn the caption into an action: chef hat, spoon, fork, flag, headband, instrument, menu, alarm clock, shopping bag, or tiny costume accessory.
- Attach a prop lightly to an existing character or place a separate mini illustration in adjacent negative space. Never paste a large colored shape across the photographed subject.
- Match the existing doodle line weight, outline color, blush palette, lighting mood, and simplified perspective. Favor airy outline drawing with only 1–2 small color fills sampled from the photo.
- Keep story-prop illustration coverage around 3–8% of the frame, even in Hero Story; the overall Hero Story overlay can reach 10–18% only because the headline and lettering are larger. Never hide the photographed object's identifying surface, label, face, or food texture.
- Do not add a full new photographed object. Story props are clearly hand-drawn overlays only.

## Integration test

- At thumbnail size, Hero Story must read as a photograph with a single lively headline and clear object characters; Light Story must read as a photograph first and an annotation layer second.
- The overlay should feel removable without leaving a compositional hole, but Hero Story may deliberately own the clean upper-third negative space.
- Reject oversized hats, utensils, badges, solid geometric stickers, rigid UI cards, or captions that sit on top of the food.

## Accuracy strategy

- For short decorative English, model-rendered lettering is acceptable after visual verification.
- For Chinese or exact copy, prefer deterministic post-production typesetting when available.
- If model-rendered text contains any wrong glyph, remove it and typeset the exact supplied text locally.
- Never ship approximate Chinese, invented characters, or unreadable pseudo-writing.

## Quality gate

- Every caption is exact, legible, and clearly associated with one object.
- Text adds personality or story rather than describing the obvious.
- The approved Kawaii Clean image is otherwise unchanged.
- Hero Story has one unmistakable headline, a readable caption hierarchy, and intentional clustered decorations. Light Story remains restrained by choice.
- The frame still reads as a photographic scene with a coherent character story, not as a generic full-cartoon sticker sheet.
