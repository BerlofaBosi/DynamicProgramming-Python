"""
Função recursiva que recebe como parâmetro uma lista de números e
retorna o somatório dos números PARES contidos na lista.
"""

def contar_pares(lista):
    if len(lista) == 0:                             # lista vazia
        return 0
    elif lista[0] % 2 == 0:                         # primeiro item é par
        return lista[0] + contar_pares(lista[1:])   # inclui item no somatório
    else:                                           # primeiro item é ímpar
        return contar_pares(lista[1:])              # não inclui item no somatório


lista = [2, 4, 6, 3, 7, 10]
print(contar_pares(lista))
