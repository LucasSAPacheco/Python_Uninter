# Aqui é a nossa lista de produtos no qual vamos nos basear para procurar os dados.
produtos = [(100, 'Cachorro-Quente', 9.0),
            (101, 'Cachorro-Quente Duplo', 11.0),
            (102, 'X-Egg', 12.0),
            (103, 'X-Salada', 13.0),
            (104, 'X-Bacon', 14.0),
            (105, 'X-Tudo', 17.0),
            (200, 'Refrigerante Lata', 5.0),
            (201, 'Chá Gelado', 4.0)]

total = 0.0

print('Bem vindo a Loja do Lucas Santana de Amorim Pacheco')
print('*' * 16, 'Cardápio', '*' * 16)
print('| Código |       Descrição       | Valor |')
for item in produtos:
    codigo = str(item[0])
    descricao = item[1]
    valor = str(item[2])
    print(f"| {codigo:^6s} | {descricao:^21s} | {valor:^5s} |")
print('*' * 42)

while True:
    codigo = int(input("Entre com o código desejado: "))
    produto_encontrado = None

# Esse "For" vai percorrer toda a lista procurando o código pessado pelo usuário.
    for produto in produtos:
        if produto[0] == codigo:
            produto_encontrado = produto
            break

# Caso o "For" anterior encontre algo, a variável produto encontrado não será mais = None, então entrará nesse "if"
# Caso não encontre ele cai no "else" e volta pro início do "while True" até o usuário digitar um código valido.
    if produto_encontrado:
        total += produto_encontrado[2]
        print(f"Você pediu um {produto_encontrado[1]} no valor de {produto_encontrado[2]:.2f}")
    else:
        print("Opção inválida!")
        continue

    resposta = int(input("Deseja pedir mais alguma coisa?\n1 - Sim\n0 - Não\n"))
# Aqui será verificado se o cliente quer continuar através da resposta, se for igual a "0", ele sai do "while"
# Caso contrário ele volta para o inicio do "while"
    if resposta == 0:
        break

print(f"\nValor total a pagar: R$ {total:.2f}")
