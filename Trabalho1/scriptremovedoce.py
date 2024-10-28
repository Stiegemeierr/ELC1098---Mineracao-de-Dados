import json
import re


arquivo_json = r'C:\Users\Gabriel\Documents\GitHub\ELC1098---Mineracao-de-Dados\Trabalho1\padaria_trab.json'


with open(arquivo_json, 'r', encoding='utf-8') as f:
    dados = json.load(f)


for item in dados:
    item["produtos"] = [
        re.sub(r"^Doce\s+\w+", "Doce", produto) if produto.startswith("Doce") else produto
        for produto in item["produtos"]
    ]


with open(arquivo_json, 'w', encoding='utf-8') as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)

print("O arquivo JSON foi atualizado com 'Doce' sem o tipo!")
