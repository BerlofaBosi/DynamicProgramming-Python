def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1


lista = ['Ana', 'Paulo', 'Pedro', 'João']
nome = input('Insira um nome que deseja buscar: ')

index = busca_linear(lista, nome)

if index != -1:
    print(f'Nome encontrado na posição {index} da lista.')
else:
    print('Nome não encontrado na lista.')

