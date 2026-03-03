lista_nomes = []
lista_idades = []

for i in range(5):
    input_nome = input(f'Insira o nome do {i+1}º cliente: ').strip()
    input_idade = int(input(f'Insira a idade do {i+1}° cliente: ').strip())

    lista_nomes.append(input_nome)
    lista_idades.append(input_idade)

print(lista_nomes)
print(lista_idades)
