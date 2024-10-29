import json

arquivo_json = r'C:\Users\gabri\OneDrive\Documentos\GitHub\ELC1098---Mineracao-de-Dados\exerc1.json'

with open(arquivo_json, 'r', encoding='utf-8') as f:
    dados = json.load(f)

for i, item in enumerate(dados, start=1):
    item["compra"] = i

with open(arquivo_json, 'w', encoding='utf-8') as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)

print("O arquivo JSON foi atualizado com o incremento de 'compra'!")
