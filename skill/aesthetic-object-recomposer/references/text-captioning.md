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

- Use casual hand-drawn lettering with slightly irregular baselines.
- Default to white or cream with a subtle dark shadow or outline.
- Use one source-derived accent color for emphasis marks only.
- Combine at most two sizes and one lettering style.
- Avoid heavy display fonts, dense bubbles, vertical typesetting, and long paragraphs.

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
