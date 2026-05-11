# Modifique o algoritmo QuickSort para ordenar listas em ordem decrescente.

import random

def particiona(lista, inicio, fim):
    indice = random.randint(inicio, fim,)
    aux = lista[inicio]
    lista[inicio] = lista[indice]
    lista[indice] = aux

    pivo = lista[inicio]
    i = inicio
    for j in range(inicio + 1, fim + 1):
        if lista[j] >= pivo:
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