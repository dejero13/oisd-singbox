# OISD NSFW Small для sing-box

Updatable oisd json and srs files for use with sing-box.

**Последнее обновление:** 2026-04-04 00:29:15 UTC  
**Количество доменов:** 19463

### Файлы
- `oisd-nsfw-small.json` — исходный формат  
- `oisd-nsfw-small.srs` — скомпилированный формат

### Использование
```json
"rule_set": [
  {
    "tag": "oisd-nsfw",
    "type": "local",
    "format": "binary",
    "path": "oisd-nsfw-small.srs"
  }
]
