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

**Five empty folders stop being shipped.** A folder now materialises in whatever
pack references it (HeroicLands/package-build#257), so one that nothing
references materialises nowhere: `Traits` (`characteristics`), `Philosophies`
(`mysteries`), and `Pregens`, `Prototypes` and `Samples` (`characters`). All five
were declared by the YAML and emitted as empty folders; none is named by a single
note. Their notes keep the authored ids, so any of them reappears — same id, same
colour, same place — the moment a note files itself there. Every other document
in every pack is byte-identical.

Requires the folder-note support in `@heroiclands/package-build`
(HeroicLands/package-build#276).
