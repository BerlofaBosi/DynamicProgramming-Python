# Utiliza-se pass quando está prototipando uma função.

def push(stack, item):
    """Insere um item na lista"""
    stack.append(item)

def pop(stack):
    """Remove um item da pilha e retorna o item removido"""
    stack.pop()

def top(stack):
    """Retorna o topo da pilha"""
    return stack[-1]

def is_empty(stack):
    """Retorna True se a pilha estiver vazia"""
    return True if len(stack) == 0 else False


def size(stack):
    """Retorna o tamanho da pilha"""
    return len(stack)


# EXERCÍCIO 2:
# Um escritório recebe documentos que precisam ser processados.
# O último documento adicionado deve ser o primeiro a ser processado.
# Peça o nome dos documentos e os adicione à uma pilha.
# Processe os documentos na ordem inversa à que foram adicionados (LIFO).
# Após processar todos os documentos, exiba "Todos os documentos foram processados!".

pilha_docs = []

while True:
    nome_doc = input('Entre com o nome do documento a ser processado: (0 -> Sair) ')
    if nome_doc == '0':
        break

    push(pilha_docs, nome_doc)

for i in range(size(pilha_docs) -1, 0, -1):
    print(f'Processando Documento: {pilha_docs[i]}')

print(f'Todos os {size(pilha_docs)} documentos foram processados!')


# EXERCÍCIO 3
# Implemente a função "verificar_balanceamento", que recebe como entrada
# uma string representando uma expressão aritmética contendo parenteses
# e verifica se os parênteses estão balanceados.
# Deve ser utilizada uma estrutura Pilha para resolver o problema.
# Se a expressão estiver balanceada, deve retornar True,
# caso contrário deve retornar False

def verificar_balanceamento(expressao):
    pilha_parenteses = []
    for i in expressao:
        if i == '(':
            push(pilha_parenteses, 'item')
        elif i == ')' :
            if is_empty(pilha_parenteses):
                return False
            pop(pilha_parenteses)

    return True if is_empty(pilha_parenteses) else False


print(verificar_balanceamento("(1)"))                       # True
print(verificar_balanceamento("(((2+3)/5) - 1)"))           # True
print(verificar_balanceamento("((((((((((()))))))))))"))    # True
print(verificar_balanceamento("(((()(((7+3)))))())"))       # True
print(verificar_balanceamento("10 / (4 - 1) * (5))"))       # False
print(verificar_balanceamento("(((())))))"))                # False
print(verificar_balanceamento("((((())))"))                 # False
print(verificar_balanceamento("))(("))                      # False
print(verificar_balanceamento(")((()))("))                  # False
