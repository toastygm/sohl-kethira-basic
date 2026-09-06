---
"sohl-kethira-basic": patch
---

**370 notes move their SoHL system fields under `sohl.system`** (#97).

This tree authored its SoHL system fields directly under `sohl:`. The content
format puts them under `sohl.system`, at the paths the compiled document actually
stores — so a note says what the document holds, and a key it does not declare is
an error rather than a silent drop.

**370 notes, 1,762 key moves, 140 null keys dropped, 0 refused.** By note type:
224 `mysticalability`, 66 `skill`, 28 `being`, 28 `affiliation`, 24 `mystery`.

```yaml
sohl:
  kbcat: script
  archetype: 0
  system: # ← new
    skillBaseFormula: sb(attr.rea, attr.per)
    masteryLevelBase: 0
    combatCategory: none
```

The move list is derived from the field declarations the compiler itself obeys,
never from a hand-written list. `kbcat`, `archetype` and the `items:` generator
stay where they are — they are toolchain and generator keys, not system fields.

**A key authored as `null` is dropped rather than moved.** At the legacy position
the compiler reads `value ?? default`, so `null` never reached a document; at the
destination it _would_ arrive, because that position returns the value as
authored. Moving it would therefore have changed the compiled output. The 140 are
`assocSkillCode` (44), `assocAffiliationCode` (44), `defaultCombatGroup` (28) and
`levelBase` (24).

**The compiled packs are byte-identical.** `build/packs-json` was compiled before
and after and diffed — 387 documents across `characteristics`, `mysteries` and
`characters`, no difference, and the compile reported the same nine diagnostics
both times.

**Lint is unchanged but for 28 warnings that stop firing, correctly.** Every
finding is identical in file, kind and count except the `title: ""` blank-heading
warning on the 28 affiliation notes. That check resolves `title` through the
`sohl:` block before the top level, so an affiliation's _office title_ was being
read as the note's _page heading_ — precisely the ambiguity this move exists to
end. No note in this tree carries a content-table query naming a moved field, so
no query needed updating.

Only the `sohl:` region of each note's frontmatter was spliced, and each file was
verified by parsing before and after and comparing the whole frontmatter against
the intended result, refusing the write on any other difference.
