---
"sohl-kethira-basic": patch
---

**Authoring changes.** The template-priority number every note carries is now
written as `data.templatePriority` rather than `archetype`, the name it shared
with an unrelated idea. The value is unchanged on all 370 notes, and the pack
folders each note already declares through `packFolder` are no longer restated
in the build configuration.

The compiled compendiums are byte-identical, so nothing changes in play.
