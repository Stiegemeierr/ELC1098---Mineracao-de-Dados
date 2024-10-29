import json

arquivo_json = r'.\padaria_trab.json'
arquivo_processado = r'.\exerc1.json'

with open(arquivo_json, 'r', encoding='utf-8') as f:
    dados = json.load(f)

for i, item in enumerate(dados, start=1):
    item["compra"] = i

with open(arquivo_processado, 'w', encoding='utf-8') as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)

print("Um arquivo JSON processado foi criado!")
