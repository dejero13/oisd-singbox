Updatable oisd json and srs files for use with sing-box.

**Последнее обновление:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC  
**Количество доменов:** {len(domains)}

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
