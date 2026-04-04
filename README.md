Updatable oisd json and srs files for use with sing-box.

### Файлы
- `oisd-nsfw-small.json` 
- `oisd-nsfw-small.srs`

### Использование
```json
"rule_set": [
  {{
    "tag": "oisd-nsfw",
    "type": "local",
    "format": "binary",
    "path": "oisd-nsfw-small.srs"
  }}
]
