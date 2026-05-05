# -------------------------------------------------
"""
EXERCÍCIO 1:
Preencha uma lista com 1000 números inteiros em ordem CRESCENTE.
Ordene a lista utilizando os métodos bubble, selection e insertion sort.
Informe para cada método:
A quantidade de operações de comparações entre elementos.
A quantidade de operações de trocas entre elementos.
"""

def bubble_sort(lista):
    comparacoes = 0
    trocas = 0

    n = len(lista)
    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            comparacoes += 1                        # Contabiliza as comparações realizadas

            if lista[j] > lista[j + 1]:             # compara itens
                trocas += 1                         # Contabiliza as trocas realizadas

                aux = lista[j]                      # realiza a troca
                lista[j] = lista[j + 1]
                lista[j + 1] = aux

    return comparacoes, trocas


def selection_sort(lista):
    comparacoes = 0
    trocas = 0

    n = len(lista)
    for i in range(0, n - 1):
        menor = i
        for j in range(i + 1, n):                   # encontra menor item
            comparacoes += 1

            if lista[j] < lista[menor]:
                trocas += 1

                menor = j
        aux = lista[i]                              # realiza a troca
        lista[i] = lista[menor]
        lista[menor] = aux

    return comparacoes, trocas


def insertion_sort(lista):
    comparacoes = 0
    trocas = 0

    n = len(lista)
    for i in range(1, n):
        comparacoes += 1

        j = i
        while j > 0 and lista[j] < lista[j - 1]:    # compara itens
            trocas += 1

            aux = lista[j]                          # realiza a troca
            lista[j] = lista[j - 1]
            lista[j - 1] = aux
            j -= 1

    return comparacoes, trocas


lista = list(range(1000))
print(lista)
bubble = bubble_sort(lista)

print('-'*30)
print('Ordenação de 1000 números inteiros em bubble sort:')
print(f'Comparações realizadas: {bubble[0]}')
print(f'Trocas realizadas: {bubble[1]}')


lista = [i for i in range(1000, 1, -1)]
selection = selection_sort(lista)

print('-'*30)
print('Ordenação de 1000 números inteiros em selection sort:')
print(f'Comparações realizadas: {selection[0]}')
print(f'Trocas realizadas: {selection[1]}')


lista = [i for i in range(1000, 1, -1)]
insertion = insertion_sort(lista)

print('-'*30)
print('Ordenação de 1000 números inteiros em insertion sort:')
print(f'Comparações realizadas: {insertion[0]}')
print(f'Trocas realizadas: {insertion[1]}')

