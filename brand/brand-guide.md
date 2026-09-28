# Brand Guide: Visual Colours

Use this for every reel, carousel, story, thumbnail and deck.

## Palette

| Role | Name | Hex | Use for |
|---|---|---|---|
| Base (darkest) | Midnight Navy | `#0a1a30` | Backgrounds, primary dark surface, text on light slides |
| Base (mid) | Deep Navy | `#16304e` | Gradient mid-stop, cards on dark backgrounds |
| Base (light) | Ocean Blue | `#2a517f` | Gradient end-stop, secondary cards, dividers |
| Accent | Steel Teal | `#6896a3` | Highlights, key numbers, icons, underlines, progress markers |
| Neutral | White | `#ffffff` | Headlines and body text on dark; light slide backgrounds |

## Signature gradients

| Name | Value | Use for |
|---|---|---|
| **Night Depth** (primary) | `linear-gradient(160deg, #0a1a30 0%, #16304e 55%, #2a517f 100%)` | Default background for reels, carousels and covers |
| **Tide** (accent) | `linear-gradient(135deg, #2a517f 0%, #6896a3 100%)` | Highlight cards, CTA buttons, "number" tiles |
| **Glow** (spotlight) | Radial `#6896a3` at 25–35% opacity over Night Depth | Behind a key number or product, to pull the eye |
| **Mist** (light variant) | `linear-gradient(180deg, #ffffff 0%, #e8eff1 100%)` with `#0a1a30` text | Occasional light slide for contrast (e.g. "the answer" slide) |

## Contrast rules (checked)

| Text colour | On background | Ratio | Rule |
|---|---|---|---|
| White | `#0a1a30` | 17.5 : 1 | ✅ Any size |
| White | `#16304e` | 13.4 : 1 | ✅ Any size |
| White | `#2a517f` | 8.1 : 1 | ✅ Any size |
| `#6896a3` | `#0a1a30` | 5.4 : 1 | ✅ Subheads, numbers, labels |
| White | `#6896a3` | 3.2 : 1 | ⚠️ **Large headlines only** (≥ 28pt bold). Never body text |
| `#0a1a30` | `#6896a3` | 5.4 : 1 | ✅ Button and tile text |
| `#0a1a30` | White | 17.5 : 1 | ✅ Any size (light slides) |

## Usage ratio
- **~70% navy gradient** (Night Depth) as the base
- **~20% white** for text and breathing space
- **~10% Steel Teal** for accents, used only where you want the eye to go (the number, the key word, the CTA)

## Applying it to content
- **Carousels:** Night Depth background, white headline, the key number or word in Steel Teal, "1/7" progress markers in Steel Teal. The CTA slide uses a Tide gradient button with navy text.
- **Reels:** on-screen text in white on a semi-transparent `#0a1a30` bar (70–80% opacity). The highlighted word is in Steel Teal. Colour grade footage slightly cool so it matches.
- **Crossed-out / "wrong" elements:** use white at 40% opacity with a Steel Teal strike-through. Avoid red, which isn't a brand colour; if you must show "wrong", use a thin white ✕.
- **Data and charts:** bars and lines in Steel Teal, gridlines in `#2a517f`, labels in white.
- **Photos and client footage:** keep them natural. Apply brand colour only in overlays, frames and text, never as a heavy filter (especially for clinic content, where edited images are restricted).

## Quick copy (for designers and tools)
```css
:root {
  --navy-900: #0a1a30;
  --navy-700: #16304e;
  --navy-500: #2a517f;
  --teal-400: #6896a3;
  --white:    #ffffff;
  --grad-night: linear-gradient(160deg, #0a1a30 0%, #16304e 55%, #2a517f 100%);
  --grad-tide:  linear-gradient(135deg, #2a517f 0%, #6896a3 100%);
}
```
