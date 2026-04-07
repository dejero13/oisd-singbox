import requests
import json
from datetime import datetime
import subprocess
import os

URL = "https://raw.githubusercontent.com/sjhgvr/oisd/main/domainswild2_nsfw_small.txt"


def main():
    print("🔄 Скачиваем свежий OISD NSFW Small...")
    r = requests.get(URL)
    r.raise_for_status()
    
    # Очищаем: убираем комментарии, пустые строки
    domains = [
        line.strip() 
        for line in r.text.strip().splitlines() 
        if line.strip() and not line.startswith('#')
    ]
    
    print(f"✅ Найдено доменов: {len(domains)}")
    
    # === JSON (source format) ===
    rule_set = {
        "version": 3,
        "rules": [
            {
                "domain_suffix": domains
            }
        ]
    }
    
    json_path = "oisd-nsfw-small.json"
    srs_path = "oisd-nsfw-small.srs"
    
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(rule_set, f, ensure_ascii=False, indent=2)
    
    print("✅ oisd-nsfw-small.json создан")

    # === Чистый TXT ===
    with open("oisd-nsfw-small.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(domains))
    
    print("✅ oisd-nsfw-small.txt создан (чистый список)")

    # === Конвертация в .srs через sing-box CLI ===
    print("🔄 Конвертируем в oisd-nsfw-small.srs...")
    try:
        result = subprocess.run([
            "sing-box", "rule-set", "compile",
            "--output", srs_path,
            json_path
        ], capture_output=True, text=True, check=True)
        
        if os.path.exists(srs_path):
            size = os.path.getsize(srs_path) / 1024
            print(f"✅ oisd-nsfw-small.srs успешно создан ({size:.1f} KB)")
        else:
            print("⚠️ Файл .srs не создан")
            
    except FileNotFoundError:
        print("❌ Ошибка: sing-box не найден в PATH. Установите sing-box и добавьте его в PATH.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка при конвертации в .srs:\n{e.stderr}")

    # === README.md ===
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(f"""# OISD NSFW Small для sing-box

Updatable oisd json, srs and txt files for use with sing-box. [OISD source](https://github.com/sjhgvr/oisd)

**Последнее обновление:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC  
**Количество доменов:** {len(domains)}

### Файлы

- JSON https://github.com/dejero13/oisd-singbox/releases/download/latest/oisd-nsfw-small.json
- SRS  https://github.com/dejero13/oisd-singbox/releases/download/latest/oisd-nsfw-small.srs
- TXT  https://github.com/dejero13/oisd-singbox/releases/download/latest/oisd-nsfw-small.txt
""")
        
print(" README.md обновлён")
print("\n Готово! Все файлы созданы.")

if __name__ == "__main__":
    main()

