# Merge Sort --> É um algoritmo eficiente de ordenação baseado na técnica de divisão e conquista.
# Divisão: Ele divide a lisat em duas metades recursivamente até obter listas unitárias.
# Conquista: Combina (merge) as listas menores de forma ordenada.
# O merge sort não tem melhor caso e pior caso, o tempo de execução dele sempre será o mesmo,
# já que independente da pre-disposição inicial da lista não o beneficiará em poupar passos.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    meio = len(arr) // 2
    esquerda = merge_sort(arr[:meio])
    direita = merge_sort(arr[meio:])
    resultado = []

    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    return resultado + esquerda[i:] + direita[j:]

lista = [5, 3, 8, 4, 2]
print("Lista ordenada: ", merge_sort(lista))

# Quick Sort --> Primeiro algoritmo eficiente que foi implementado.
# O quick sort também é baseado na técnica de divisão e conquista. É baseado em uma rotina fundamental chamada de particionamento.
# Particionamento: Escolhe um item na lista chamado de pivô (geralmente o primeiro ou último item)
# |--> Organiza os elementos menores que o pivô à esquerda e os maiores à direita.

# *Curiosidade: O python atualmente utiliza o power sort, que é mais eficiente que os dois métodos apresentados nesse arquivo.

import random

def particiona(lista, inicio, fim):
    indice = random.randint(inicio, fim,)
    aux = lista[inicio]
    lista[inicio] = lista[indice]
    lista[indice] = aux

    pivo = lista[inicio]
    i = inicio
    for j in range(inicio + 1, fim + 1):
        if lista[j] <= pivo:
            i += 1
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

    aux = lista[inicio]
    lista[inicio] = lista[i]
    lista[i] = aux
    return i

def quick_sort(lista, inicio, fim):
    if (inicio < fim):
        posicao = particiona(lista, inicio, fim)
        quick_sort(lista, inicio, posicao - 1)
        quick_sort(lista, posicao + 1, fim)
    return lista

lista = [5, 3, 8, 4, 2]
print("Lista ordenada: ", quick_sort(lista, 0, len(lista) - 1))
