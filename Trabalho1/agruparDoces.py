import json
import re


arquivo_processado = r'.\exerc1.json'
arquivo_doces = r'.\exerc2.json'

with open(arquivo_processado, 'r', encoding='utf-8') as f:
    dados = json.load(f)

for item in dados:
    item["produtos"] = [
        re.sub(r"^Doce\s+\w+", "Doce", produto) if produto.startswith("Doce") else produto
        for produto in item["produtos"]
    ]

with open(arquivo_doces, 'w', encoding='utf-8') as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)

print("Um arquivo JSON com os doces agrupados foi criado!")
