def bubble_sort(lista):
    n = len(lista)
    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            if lista[j] > lista[j + 1]:             # compara itens
                aux = lista[j]                      # realiza a troca
                lista[j] = lista[j + 1]
                lista[j + 1] = aux


def selection_sort(lista):
    n = len(lista)
    for i in range(0, n - 1):
        menor = i
        for j in range(i + 1, n):                   # encontra menor item
            if lista[j] < lista[menor]:
                menor = j
        aux = lista[i]                              # realiza a troca
        lista[i] = lista[menor]
        lista[menor] = aux


def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        j = i
        while j > 0 and lista[j] < lista[j - 1]:    # compara itens
            aux = lista[j]                          # realiza a troca
            lista[j] = lista[j - 1]
            lista[j - 1] = aux
            j -= 1


# -------------------------------------------------
lista = [6, 7, 4, 1, 3, 2, 5]
bubble_sort(lista)
print(lista)

lista = [1, 2, 3, 4, 5, 6, 7]
bubble_sort(lista)
print(lista)

lista = [7, 6, 5, 4, 3, 2, 1]
bubble_sort(lista)
print(lista)


# -------------------------------------------------
lista = [6, 7, 4, 1, 3, 2, 5]
selection_sort(lista)
print(lista)

lista = [1, 2, 3, 4, 5, 6, 7]
selection_sort(lista)
print(lista)

lista = [7, 6, 5, 4, 3, 2, 1]
selection_sort(lista)
print(lista)


# -------------------------------------------------
lista = [6, 7, 4, 1, 3, 2, 5]
insertion_sort(lista)
print(lista)

lista = [1, 2, 3, 4, 5, 6, 7]
insertion_sort(lista)
print(lista)

lista = [7, 6, 5, 4, 3, 2, 1]
insertion_sort(lista)
print(lista)
