def busca_estoque(estoque, produto):
    contador = 0
    while contador < len(estoque):
        if estoque[contador] == produto:
            return contador
        contador += 1
    else:
        return -1


estoque = [
    'Amaciante',
    'Sabão em pó',
    'Pasta de Dente',
    'Shampoo',
    'Condicionador',
    'Creme',
    'Máscara Hidratante'
]

produto = input('Qual produto deseja verificar no estoque? ')

index = busca_estoque(estoque, produto)

if index != -1:
    print(f'Produto encontrado na posição {index} do estoque.')
else:
    print('Produto não encontrado no estoque.')

