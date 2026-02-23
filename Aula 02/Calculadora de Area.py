import math

print('''
1 - Círculo
2 - Retângulo
''')

opcao = int(input('Escolha sua opção: '))

match opcao:
    case 1:
        raio = float(input('Informe o raio do círculo em mm: '))

        area = math.pi * raio ** 2
        print(f'A área do círculo é igual a {area:.2f}mm.')

    case 2:
        x = float(input('Informe o lado x do retângulo em mm: '))
        y = float(input('Informe o lado y do retângulo em mm: '))

        area = x * y
        print(f'A área do retângulo é igual a {area:.2f}mm.')

    case _:
        print('Opção inválida.')
