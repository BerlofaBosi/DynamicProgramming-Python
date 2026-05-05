"""
Escreva uma função recursiva que recebe como parâmetros dois números inteiros
e retorna o resultado da multiplicação entre esses dois números.
Realize o cálculo utilizando somas sucessivas.
Por exemplo:
4*5 = 5+5+5+5 = 20
3*5 = 5+5+5 = 15
2*5 = 5+5 = 10
1*5 = 5
0*5 = 0
"""

def multiplicar(a, b):
    if a == 0:          # qualquer número multiplicado por zero, retorna zero
        return 0
    else:
        return b + multiplicar(a-1, b)

print(multiplicar(4, 5))

"""
multiplicar(4, 5)  =  5 + multiplicar(3, 5)  =  5 + 15  =  20
multiplicar(3, 5)  =  5 + multiplicar(2, 5)  =  5 + 10  =  15
multiplicar(2, 5)  =  5 + multiplicar(1, 5)  =  5 + 5   =  10
multiplicar(1, 5)  =  5 + multiplicar(0, 5)  =  5 + 0   =  5 
multiplicar(0, 5)  =  0
"""
