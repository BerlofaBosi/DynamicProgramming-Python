# exemplo de lista
frutas = ['maçã', 'banana', 'laranja', 'abacaxi']

# percorrer itens da lista
for i in frutas:
    print(i)

# percorrer itens acessando os indices
for i in range(len(frutas)):
    print(frutas[i])

# inserir itens na lista (quantidade previamente definida)
quantidade = int(input('Informe a quantidade de itens: '))
lista = []
for i in range(quantidade):
    numero = float(input('Informe um número: '))
    lista.append(numero)
print(lista)

# inserir itens na lista (quantidade indefinida)
lista = []
while True:
    numero = float(input('Informe um número (-1 para finalizar): '))
    if numero == -1:
        break
    lista.append(numero)
print(lista)

# remover item da lista (pop)
frutas = ['maçã', 'banana', 'laranja', 'abacaxi']
frutas.pop()        # remove o último item
print(frutas)

frutas.pop(0)       # remove o index informado
print(frutas)

# remover item da lista (remove)
frutas = ['maçã', 'banana', 'laranja', 'abacaxi']
if 'pera' in frutas:
    frutas.remove('pera')
print(frutas)
