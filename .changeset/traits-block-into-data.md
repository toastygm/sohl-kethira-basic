---
"sohl-kethira-basic": patch
---

**Seventeen being notes move their `traits:` block into `data:`** (#95).

The eleven bandits, the five pregenerated characters and `HMK_Basic_Folk`
described their subject in a top-level `traits:` block the content format does
not declare. Top level is open — the format passes unrecognised keys through to
Hugo — so nothing checked a key written there, and a misspelling under `traits:`
silently became a theme parameter. `data:` is closed, so the same misspelling now
names the note and suggests the key it was meant to be.

Every field moves to where `being` declares it, and three change shape as well as
place:

```yaml
data:
  gender: male # was traits.gender
  age: 41 # was traits.age
  birthday: 678/1/7 # was traits.birthday
  height: 1.73 # was traits.height.m
  weight: 65.77 # was traits.weight.kg
  frame: medium # was traits.build.frame
  appearance: # was traits.appearance, unchanged
    eye_color: brown
```

**The compiled packs are byte-identical.** None of these fields is compiled into
a Foundry document, so no emitted document changes: `build/packs-json` was
compiled before and after and diffed — 370 files, no difference.

**Two out-of-vocabulary values are carried across verbatim, not rewritten.**
`gender: unknown` on 14 of the 17 notes, where the format declares
`male | female | other`; and one `frame: slight`, where the format declares
`scant | light | medium | large | massive` — `slight` looks like `scant` or
`light` and nothing can say which. (The single `frame: large` is valid.) Moving
them unchanged keeps each note saying exactly what its author wrote; choosing a
replacement would be inventing data. Settling them is separate work.

Only the `traits:` region of each note's frontmatter was spliced; no other key,
note body, or file was touched.
