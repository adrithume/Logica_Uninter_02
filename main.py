# Identificação
print('Bem-vindo a Lanchonete da Adriana C. G. Thume RU 1902469')

# Descrição dos produtos
print(('*'*15)+'Cardápio'+('*'*15))
print("| Código |          Descrição          | Valor |")
print("|  100   |       Cachorro-Quente       |  9,00 |")
print("|  101   |    Cachorro-Quente Duplo    | 11,00 |")
print("|  102   |            X-Egg            | 12,00 |")
print("|  103   |           X-Salada          | 13,00 |")
print("|  104   |           X-Bacon           | 14,00 |")
print("|  105   |           X-Tudo            | 17,00 |")
print("|  200   |     Refrigerante Lata       |  5,00 |")
print("|  201   |         Chá Gelado          |  4,00 |")

contador = 0 # Para contar a quantidade de pedidos
total = 0 # Total a ser pago pelo cliente

while True:
    # Entrada de dados pelo usuário
    pedido = input('Entre com o código desejado: ')

    if pedido == '100':
        produto = 'Cachorro-Quente'
        valor = 9.00
    elif pedido == '101':
        produto = 'Cachorro-Quente Duplo'
        valor = 11.00
    elif pedido == '102':
        produto = 'X-Egg'
        valor = 12.00
    elif pedido == '103':
        produto = 'X-Salada'
        valor = 13.00
    elif pedido == '104':
        produto = 'X-Bacon'
        valor = 14.00
    elif pedido == '105':
        produto = 'X-Tudo'
        valor = 17.00
    elif pedido == '200':
        produto = 'Refrigerante Lata'
        valor = 5.00
    elif pedido == '201':
        produto = 'Chá Gelado'
        valor = 4.00
    else:
        print('Opção Inválida')
        continue # Volta para o começo do while

    # Saída de dados
    print('Você pediu um ' + produto + ' no valor de {:.2f}'.format(valor))
    contador = contador + 1
    total = total + valor # Somatório dos pedidos
    print('Deseja pedir mais alguma coisa?')
    print('1 - Sim')
    print('0 - Não')
    pedido2 = input('') # Nova entrada de dados

    if pedido2 == '1':
        continue # Volta para o começo do while
    else:
        print('O total a ser pago é: {:.2f}'.format(total))
        break