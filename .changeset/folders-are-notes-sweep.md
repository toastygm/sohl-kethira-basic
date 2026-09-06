---
"sohl-kethira-basic": minor
---

**This tree's folders are notes** (#91).

The three `assets/content/*-folders.yaml` files are gone. Each of the 22 folders
is a `type: folder` note under `assets/content/Folders/`, and the 359 notes that
named a folder by its Foundry id name it by address instead:

```yaml
packFolder: affiliations # was: folder: <16-char id>
```

**Every folder keeps its authored `id`**, so a world already holding these
folders goes on resolving them — this is a build change, not a world migration.

**The defect this fixes.** This tree has no `journal-folders.yaml` at all, so
the six item folders its documentation journals are filed in were declared by no
journals pack — dangling references, silently. A folder now materialises in every
pack that references it (HeroicLands/package-build#257), so the journals pack
gets them without a second folder file to keep in step.

Requires the folder-note support in `@heroiclands/package-build`
(HeroicLands/package-build#276).
