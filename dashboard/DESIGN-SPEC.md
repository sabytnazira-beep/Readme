# Dashboard design spec: Strategy → Matrix screen

Paste this whole file into Claude in VS Code together with the file(s) for the Matrix screen. Words like "futuristic" or "clean" leave too much open, so Claude falls back to its default look: white page, grey text, blue buttons. This spec names every decision instead.

Reference prototype: `dashboard/matrix-console.html` (open it in a browser). Match its look and behaviour.

---

## 1. Design tokens (use these, no other colours)

```css
:root {
  --navy-950:#06111f;  /* app background */
  --navy-900:#0a1a30;  /* panels, inputs */
  --navy-700:#16304e;  /* raised cards */
  --navy-500:#2a517f;  /* dividers, secondary fills */
  --teal:#6896a3;      /* accent: numbers, active state, progress */
  --teal-hi:#8fb7c2;   /* focus ring, glow */
  --ink:#ffffff; --ink-2:rgba(255,255,255,.72); --ink-3:rgba(255,255,255,.48);
  --line:rgba(104,150,163,.18); --line-2:rgba(104,150,163,.34);
  --grad-night:linear-gradient(160deg,#0a1a30 0%,#16304e 55%,#2a517f 100%);
  --grad-tide:linear-gradient(135deg,#2a517f 0%,#6896a3 100%);
  --ok:#7fc8a9;   /* status only: script-ready */
  --warn:#e2c07a; /* status only: stale / missing */
  --ease:cubic-bezier(.2,.8,.2,1);
}
```

- Dark UI only. Page = `--navy-950` with `--grad-night` overlay and a faint 48px teal grid, masked to fade out.
- Primary buttons = `--grad-tide` with `#0a1a30` text. Never white text on teal.
- Ratio: ~70% navy, ~20% white text, ~10% teal. Teal marks only what needs attention.
- Fonts: Sora (headings), IBM Plex Sans (body), JetBrains Mono (IDs, counts, labels). Use `tabular-nums` on all numbers.
- Uppercase mono labels: 11px, letter-spacing .12em, `--ink-3`.

## 2. Layout: three columns

| Column | Width | Contents |
|---|---|---|
| Pipeline rail | 260px | Client pack meter (7/8 + gradient bar). Then **Research → Decide → Plan** as a vertical stepper with one node per document: filled teal = done, amber ring = stale, white glowing = current. |
| Main | fluid | Stale-source alert → header → Signal ladder → rows |
| Inspector | 360px, sticky | Details of the selected row (see §5) |

Top bar is sticky, blurred (`backdrop-filter: blur(14px)`): logo with a pulsing teal dot, breadcrumbs, ⌘K command button.
At <1180px the inspector moves under main. At <780px everything stacks to one column.

## 3. Signal ladder (replaces the 5 flat cards)

- Five rungs in a row joined by a thin wire: Share → Save → Watch → Profile → Convert.
- Each rung = a **progress ring** (78px SVG, 5px stroke, teal on 8% white) with `count/target` in mono in the middle, then name, then "`x/y SCRIPT-READY`" in teal mono, then one line of purpose.
- A soft teal light pulse travels along the wire on a 3.6s loop (this shows reach flowing toward conversion).
- Rings animate from 0 to their value on load (1s, `--ease`).
- Clicking a rung filters the rows to that stage. The active rung's core fills with `--grad-tide` and glows. Click again to clear.
- Above the rungs: "Target mix **4 / 2 / 2 / 1 / 1** · on plan".

## 4. Rows

Each row is a card with a 4-column grid:
1. **ID** (`S1`, teal mono) with the rung name under it in tiny caps.
2. **Hook** (14.5px), segment name under it in mono `--ink-3`.
3. **Cell meter**: 8 small bars, one per matrix cell (Target person, Current state, Hook, Retention, IG signal, Profile bridge, Commercial bridge, Next action). Filled = teal. Then `6/8`.
4. **Status pill**: green dot "Script-ready" when 8/8, amber dot "Needs 2" otherwise.

Filter chips above the rows: All / Missing cells / Script-ready.
Hover: border brightens, row slides 2px right. Selected: teal border plus 3px inset teal bar on the left.
Rows enter with a 40ms stagger (fade + 8px rise).

## 5. Inspector (selected row)

- **9:16 reel cover preview** (200px wide) rendered in brand colours: Night Depth background, radial teal glow, rung + segment label in teal mono, the hook in white Sora with the key word in teal, the CTA as a Tide tile, 5-dot progress bar. This is how the post will look.
- 70/20/10 colour ratio bar.
- All 8 cells as a definition list. Empty cells are amber: "Empty. Generate or type it."
- Button "Write script from this row". Disabled until 8/8.
- The panel animates in (fade + 6px rise) whenever the selection changes.

## 6. Stale-source alert

One amber-bordered strip instead of the long grey sentence: amber glowing dot, "**2 sources are older than the brief** saved Sep 22, 13:26. Positioning and Reverse Engineer still reflect the previous brief, so 3 rows below may drift." plus a "↻ Regenerate 2" button. Stale docs also show an amber ring in the rail.

## 7. Speed and keyboard

- ⌘K / Ctrl+K opens a command menu: jump to any row by ID or hook, switch stage, filter, generate.
- `J` / `K` move the selection through visible rows.
- "Generate rows" and "Regenerate" run a teal light sweep down the row list, then show a toast with the result ("10 rows checked against the 4/2/2/1/1 mix").
- Remember the chosen rung, filter and selected row between visits.

## 8. Motion rules

- One easing everywhere: `cubic-bezier(.2,.8,.2,1)`. 200–500ms for UI, 1s for ring fills.
- Ambient motion is limited to two things: the pulsing logo dot and the ladder wire pulse.
- Wrap everything in `@media (prefers-reduced-motion: reduce)` and turn animation off there.

## 9. Content rules (from CLAUDE.md)

- Any sample rows or numbers must be labelled as examples.
- No red. Warnings use amber `#e2c07a`; "wrong" content uses white at 40% with a teal strike-through.

## 10. Prompt to use in VS Code

> Rebuild the Strategy → Matrix screen to match `dashboard/DESIGN-SPEC.md` and the reference prototype `dashboard/matrix-console.html`. Keep the existing data layer and API calls; replace only the layout, styles and interaction. Follow the tokens exactly and add no other colours. Build it in this order: tokens → 3-column shell → signal ladder → rows → inspector → ⌘K menu → motion. After each step, show me a screenshot before continuing.
