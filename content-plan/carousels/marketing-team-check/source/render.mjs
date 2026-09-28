// Renders every <section class="slide"> in slides.html to ../png/slide-XX.png (1080 x 1350).
// Run: node render.mjs   (needs the `playwright` package)
import { chromium } from 'playwright';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';

const here = path.dirname(fileURLToPath(import.meta.url));
const out = path.join(here, '..', 'png');
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
await page.goto(pathToFileURL(path.join(here, 'slides.html')).href);
await page.evaluate(() => document.fonts.ready);
const slides = await page.$$('section.slide');
for (const [i, el] of slides.entries()) {
  const file = path.join(out, `slide-${String(i + 1).padStart(2, '0')}.png`);
  await el.screenshot({ path: file });
  console.log(file);
}
await browser.close();
