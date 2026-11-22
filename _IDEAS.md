# energycode.org: ideas to improve the site (2026-10-26)

The site looks plain because it uses Quarto's `lux` theme almost unchanged.
Your own work is colourful (the hex sticker, the circuit logo, the plots) but
the site around it is grey, all capitals and has square boxes.

## 1. Give it its own look

- [ ] **One brand colour.** Take the cyan→green from the logos (`#28d2f0` →
  `#78dc50`) and use it for links, tags, hover effects and a thin line under
  the navbar. A small `custom.scss` on top of `lux` will do it.
- [ ] **Better fonts.** `lux` puts every title in spaced-out capitals, so long
  titles take four lines. Use normal capitalisation with a modern font, e.g.
  *Inter* / *Source Sans 3* for titles, *Source Serif* for body text and
  *JetBrains Mono* for code.
- [ ] **Put the logo in the navbar** next to "ENERGYCODE"
  (`assets/img/logo/web_logo.png`).

## 2. Home page

- [ ] **Short introduction at the top**: one line like "Mathematics, data
  science and scientific computing in R and Python" and three buttons
  (Posts · Projects · About).
- [ ] **Show the 3 newest projects on the home page**, above the posts.

## 3. Cards

- [ ] Rounded corners, a soft shadow that lifts on hover, no border, and
  **one image shape for all cards** (e.g. 16:9 with a background colour).
- [ ] **Too many tags**: show at most 2 on the card.
- [ ] **Clean up the categories**: merge *Math* / *Mathematics*,
  *Determinant* / *Linear Algebra* / *Matrices*; drop one-offs like *Latex*,
  *Numpy*. About 8 main ones, the same set on posts and projects.

## 4. Post pages

- [ ] **Title area**: dark navy (logo colour) with white titles instead of
  grey on black.
- [ ] **Don't start with a large image** (e.g. the Tartaglia portrait in
  "Binomial Matrix" fills the first screen). Smaller or floated beside the text.
- [ ] **Mark the language**: 6 posts in Spanish, 7 in English. Add an ES/EN
  label or a language category.

## 5. Content problems

- [ ] **6 of the 14 posts are drafts** (repunits, GCD identity, triangular
  matrices, cylindrical tank, numerators/denominators, blog features). The blog
  shows only 8 and its newest is from January 2026.
- [ ] **Two dates in the wrong format**: `"01-26-2026"` and `'08-01-2023'` are
  month first; change to `YYYY-MM-DD`.
- [ ] "Binomial Matrix (I)" is dated **2009**: check it is the intended date.
- [ ] **Stack Overflow badge on About doesn't load** (Stack Overflow blocks it
  on other sites). Replace with a normal link or a shields.io badge.
- [ ] **Footer**: repeat the social icons and add an RSS link.

## 6. Small polish

- [ ] On a phone the navbar takes two rows: hide the social icons on small
  screens.
- [ ] Turn on `open-graph` and `twitter-card` in `_quarto.yml` for link
  previews.
- [ ] Add a "Featured" or "Start here" section (e.g. the OEIS posts).

## Suggested first step

Do **1 + 3** together: a `custom.scss` with colours and fonts plus the card
styling. One file and a line in `_quarto.yml`; render and compare before/after
screenshots before committing.
