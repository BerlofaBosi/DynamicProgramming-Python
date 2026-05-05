def busca(lista, item, inicio, fim):
    if fim < inicio:
        return -1
    else:
        meio = (inicio + fim) // 2
        if lista[meio] == item:
            return meio
        elif lista[meio] > item:
            return busca(lista, item, inicio, meio-1)
        else:
            return busca(lista, item, meio+1, fim)

lista = [1, 2, 4, 6, 8, 9, 10]
print(busca(lista, 9, 0, len(lista)-1))
