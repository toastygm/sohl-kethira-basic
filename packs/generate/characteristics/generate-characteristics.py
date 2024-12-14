#!./venv/bin/python3

import yaml
import json
import argparse
from unidecode import unidecode
from mergedeep import merge
import re

parser = argparse.ArgumentParser()
parser.add_argument("outputDir", help="folder where generated files should be placed")
args = parser.parse_args()

stats = {
    "systemId": "sohl",
    "systemVersion": "0.9.0",
    "coreVersion": "12.330",
    "createdTime": 0,
    "modifiedTime": 0,
    "lastModifiedBy": "TMJsvJWT6ytpHZ0M",
}

with open("./data/traits.yaml", "r", encoding="utf8") as infile:
    traitsData = yaml.safe_load(infile)

for trait in traitsData:
    print(f"Processing trait {trait['name']}")
    fname = trait["name"] + "_" + trait["id"]
    fname = unidecode(fname)
    fname = re.sub(r"[^0-9a-zA-Z]+", "_", fname) + ".json"
    pname = args.outputDir + "/" + fname

    out = {
        "name": trait["name"],
        "type": "trait",
        "img": trait["img"],
        "_id": trait["id"],
        "system": {
            "subType": trait["subType"],
            "notes": "",
            "textReference": "",
            "description": trait["description"],
            "macros": trait["macros"],
            "nestedItems": [],
            "transfer": False,
            "abbrev": trait["abbrev"],
            "skillBaseFormula": trait["skillBaseFormula"],
            "masteryLevelBase": 0,
            "improveFlag": False,
            "textValue": trait["textValue"],
            "isNumeric": trait["isNumeric"] == "TRUE",
            "intensity": trait["intensity"],
            "max": trait["max"],
            "valueDesc": trait["valueDesc"],
            "choices": trait["choices"],
        },
        "effects": [],
        "ownership": {"default": 3},
        "flags": trait["flags"],
        "_stats": stats,
        "folder": trait["folderId"],
        "_key": "!items!" + trait["id"],
    }
    with open(pname, "w", encoding="utf8") as outfile:
        json.dump(out, outfile, indent=2, ensure_ascii=False)


with open("./data/skills.yaml", "r", encoding="utf8") as infile:
    skillsData = yaml.safe_load(infile)

for skill in skillsData:
    print(f"Processing skill {skill['name']}")
    fname = skill["name"] + "_" + skill["id"]
    fname = unidecode(fname)
    fname = re.sub(r"[^0-9a-zA-Z]+", "_", fname) + ".json"
    pname = args.outputDir + "/" + fname

    merge(
        skill["flags"],
        {
            "sohl": {
                "legendary": {
                    "initSkillMult": skill["initSM"],
                    "expertiseParentSkill": skill.get("expertiseParentSkill", ""),
                },
            },
        },
    )
    out = {
        "name": skill["name"],
        "type": "skill",
        "img": skill["img"],
        "_id": skill["id"],
        "system": {
            "subType": skill["subType"],
            "notes": "",
            "textReference": "",
            "description": skill["description"],
            "macros": skill["macros"],
            "nestedItems": [],
            "transfer": False,
            "abbrev": skill["abbrev"],
            "skillBaseFormula": skill["skillBaseFormula"],
            "masteryLevelBase": 0,
            "improveFlag": False,
            "weaponGroup": skill["weaponGroup"],
            "domain": skill["domain"],
            "baseSkill": skill["baseSkill"],
        },
        "effects": skill["effects"],
        "ownership": {"default": 3},
        "flags": skill["flags"],
        "_stats": stats,
        "folder": skill["folderId"],
        "_key": "!items!" + skill["id"],
    }
    with open(pname, "w", encoding="utf8") as outfile:
        json.dump(out, outfile, indent=2, ensure_ascii=False)

with open("./data/folders.yaml", "r", encoding="utf8") as infile:
    foldersData = yaml.safe_load(infile)

for folder in foldersData:
    print(f"Processing Folder {folder['name']}")
    fname = folder["name"] + "_" + folder["id"]
    fname = unidecode(fname)
    fname = re.sub(r"[^0-9a-zA-Z]+", "_", fname) + ".json"
    pname = args.outputDir + "/" + fname

    out = {
        "name": folder["name"],
        "sorting": "a",
        "folder": folder["parentFolderId"] or None,
        "type": "Item",
        "_id": folder["id"],
        "sort": 0,
        "color": folder["color"],
        "flags": {},
        "_stats": stats,
        "_key": "!folders!" + folder["id"],
    }
    with open(pname, "w", encoding="utf8") as outfile:
        json.dump(out, outfile, indent=2, ensure_ascii=False)
