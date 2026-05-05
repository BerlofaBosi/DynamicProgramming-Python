import json

def exibe_nomes(dicionario):
    if 'filhos' not in dicionario:          # se a pessoa não tem filhos
        print(dicionario['nome'])
    else:                                   # se a pessoa tem filhos
        print(dicionario['nome'])
        for dic in dicionario['filhos']:    # percorre lista de filhos
            exibe_nomes(dic)


arquivo = input('Nome arquivo: ')
with open(arquivo+'.json', 'r', encoding='utf-8') as file:
    dicionario = json.load(file)
    exibe_nomes(dicionario)
