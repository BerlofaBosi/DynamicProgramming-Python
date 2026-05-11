# Modifique o algoritmo MergeSort para ordenar listas em ordem decrescente.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    meio = len(arr) // 2
    esquerda = merge_sort(arr[:meio])
    direita = merge_sort(arr[meio:])
    resultado = []

    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] > direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    return resultado + esquerda[i:] + direita[j:]

lista = [5, 3, 8, 4, 2]
print("Lista ordenada: ", merge_sort(lista))