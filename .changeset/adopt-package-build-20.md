---
"sohl-kethira-basic": patch
---

**Authoring changes.** A being's item entries now name the item they copy with
`model:`, an address, rather than the `shortcode:`/`type:` pair that did the same
job less precisely — one word that both selected a template and named the
compiled item's identity, with no way to say which package the template came
from. Where an entry reaches into the `sohl` package for a piece of gear, the
address now says so and follows that package's shortcodes, which are lowercase.

```yaml
# before
- { shortcode: chrm, type: skill, system: { masteryLevelBase: 39 } }
- { shortcode: RndSh, type: weapongear }
# after
- { model: skill-chrm, system: { masteryLevelBase: 39 } }
- { model: weapongear-rndsh }
```

The compiled compendiums are byte-identical, so nothing changes in play.
