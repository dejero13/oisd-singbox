import requests
import json
from datetime import datetime

URL = "https://raw.githubusercontent.com/sjhgvr/oisd/main/domainswild2_nsfw_small.txt"

def main():
    print("🔄 Скачиваем свежий OISD NSFW Small...")
    r = requests.get(URL)
    r.raise_for_status()
    
    domains = [
        line.strip() 
        for line in r.text.strip().splitlines() 
        if line.strip() and not line.startswith('#')
    ]
    
    print(f"✅ Найдено доменов: {len(domains)}")
    
    rule_set = {
        "version": 3,
        "rules": [
            {
                "domain_suffix": domains
            }
        ]
    }
    
    with open("oisd-nsfw-small.json", "w", encoding="utf-8") as f:
        json.dump(rule_set, f, ensure_ascii=False, indent=2)
    
    print("✅ oisd-nsfw-small.json создан")
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(f"""# OISD NSFW Small для sing-box

Автоматически обновляется каждый день.

**Последнее обновление:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC  
**Количество доменов:** {len(domains)}

### Файлы
- `oisd-nsfw-small.json` — исходный формат  
- `oisd-nsfw-small.srs` — скомпилированный формат

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
