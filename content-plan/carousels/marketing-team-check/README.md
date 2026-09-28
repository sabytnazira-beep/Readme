# Carousel: Is your marketing team doing a good job?

**Signal-ladder level:** Save (checklist format, with a "Save for later" pill on every slide). Slide 10 also works as a Convert prompt ("DM AUDIT").

- 10 slides, 1080 × 1350 px (4:5), ready to upload: [`png/`](png/)
- All slides in one download: [`marketing-team-check-carousel.zip`](marketing-team-check-carousel.zip)
- Source: [`source/build.py`](source/build.py) writes `slides.html`, and [`source/render.mjs`](source/render.mjs) exports the PNGs. To edit copy, change `build.py`, then run `python3 build.py && node render.mjs` (needs the `playwright` npm package).

| # | Slide | Background |
|---|---|---|
| 1 | Cover: "Every business needs to know", with a white line running off the right edge | Night Depth |
| 2 | Map: "…if their marketing team is doing a good job." The line splits into 6 branches | Night Depth |
| 3 | #1 Cost per customer | White (Mist) |
| 4 | #2 Enquiries → customers | White (Mist) |
| 5 | #3 Reply time | White (Mist) |
| 6 | #4 Repeat customers | White (Mist) |
| 7 | #5 Shares, not likes | White (Mist) |
| 8 | #6 Reports in AED | White (Mist) |
| 9 | Scorecard: 6 questions, closing line "Can’t answer? That’s the problem." | Night Depth |
| 10 | CTA: "Not sure what your numbers are?" with a DM "AUDIT" button; the line from slide 1 comes back and ends beside it | Night Depth |

## Colour notes (see `brand/brand-guide.md`)
- Slides 3–8 have a title, one short line and a side-by-side pair with no captions. The left side (✕, navy line art at 40%) is the bad sign; the right side (✓, Steel Teal `#6896a3`) is the good sign.
- Text inside the good-sign art is `#2a517f`, because small teal text on white is only 3.2:1.
- A thin teal line runs along the bottom of slides 3–8 to keep people swiping.
- Slide 9's teal closing line is large bold text, which keeps it readable on the gradient.
- The CTA uses the Tide gradient, weighted towards teal so the `#0a1a30` button text has enough contrast.
- AED 200 → 160 (slide 3) and 3 hours / 2 minutes (slide 5) are marked on the slide as examples, not client results.
