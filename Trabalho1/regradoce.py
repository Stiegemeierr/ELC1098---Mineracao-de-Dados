import json
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

arquivo_json = r'.\exerc2.json'

meuSet = set()
data = []

with open(arquivo_json, 'r', encoding='utf-8') as f:
    dados = json.load(f)

for i, item in enumerate(dados):
    for compra in item["produtos"]:
        meuSet.add(compra)

ordered_items = sorted(list(meuSet))

for i, item in enumerate(dados):
    data.append([False] * len(ordered_items))
    for j, produto in enumerate(ordered_items):
        if(produto in item["produtos"]):
            data[i][j] = True

df = pd.DataFrame(data, columns=ordered_items)

df.to_csv('dataFrameDoce.csv', index=False)

frequent_itemsets = apriori(df, min_support=0.03, use_colnames=True)

rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.3)

regras_consequentes = rules[rules['consequents'].apply(lambda x: 'Doce' in x)]

print("Conjuntos frequentes:")
print(frequent_itemsets)

print("\nRegras onde 'Doce' é um consequente:")
print(regras_consequentes)