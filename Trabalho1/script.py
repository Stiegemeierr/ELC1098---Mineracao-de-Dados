import json

# Caminho do arquivo JSON
arquivo_json = r'C:\Users\Gabriel\Documents\GitHub\ELC1098---Mineracao-de-Dados\Trabalho1\padaria_trab.json'


# Abrir e carregar o conteúdo do arquivo JSON
with open(arquivo_json, 'r', encoding='utf-8') as f:
    dados = json.load(f)

# Incrementar o valor de "compra" em cada entrada
for i, item in enumerate(dados, start=1):
    item["compra"] = i

# Salvar o JSON atualizado
with open(arquivo_json, 'w', encoding='utf-8') as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)

print("O arquivo JSON foi atualizado com o incremento de 'compra'!")
