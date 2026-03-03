lista = [4, 6, 7, 8, 10, 50, 40]
numero - int(input('Informe um numero: '))

indice = -1

for i in range(len(lista)):
    if lista[i] == numero:
        indice = i
        break

if indice != -1:
    print(f'Numero encontrado no index {indice}')
else:
    print(f'Numero não encontrado na lista.')

