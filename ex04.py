print('Bem vindo a Bicicletaria do Lucas Santana de Amorim Pacheco')
dict_pecas = {}
cod_peca = 0


# Função criada para retornar um item para o dicionário
def cadastrarPeca(index):
    while True:
        try:
            peca = {}
            nome = input("Por favor entre com o NOME da peça: ").lower()
            fabricante = input("Por favor entre com o FABRICANTE da peça: ").lower()
            preco = float(input("Por favor entre com o VALOR da peça: "))
            peca[index] = (nome, fabricante, preco)
            return peca
        except ValueError:
            print('Dados digitados invalidos!')


# Função criada para fazer consulta das peças
def consultarPeca(dict_consultar_pecas):
    while True:
        try:
            opcao = int(input('Escolha a opção desejada:\n'
                              '1. Consultar Todas as Peças\n'
                              '2. Consultar Peças por Código\n'
                              '3. Consultar Peças por Fabricante\n'
                              '4. Retornar\n'))
            if opcao == 1:
                print('-' * 15)
                for codigo, item in dict_consultar_pecas.items():
                    nome, fabricante, preco = item
                    print(f'Código: {codigo}\n'
                          f'Nome: {nome}\n'
                          f'Fabricante: {fabricante}\n'
                          f'Preço: {preco:.1f}')
                    print('-' * 15)
                continue
            # Variável "Control" criada apenas para saber se entrou no "If"
            elif opcao == 2:
                control = 0
                codigo_da_peca = int(input('Digite o código da peça: '))
                for codigo, item in dict_consultar_pecas.items():
                    nome, fabricante, preco = item
                    if codigo == codigo_da_peca:
                        control += 1
                        print('-' * 15)
                        print(f'Código: {codigo}\n'
                              f'Nome: {nome}\n'
                              f'Fabricante: {fabricante}\n'
                              f'Preço: {preco:.1f}')
                        print('-' * 15)
                # Caso não tenha entrado ela informa que não existe peça com o código digitado
                if control == 0:
                    print('Não foi encontrada nenhuma peça cadastrada com esse código')
                    continue
            # Aqui utilizei a mesma situação sobre a variável de controle "control"
            elif opcao == 3:
                control = 0
                fabricante_da_peca = input('Digite o fabricante da peça: ')
                for codigo, item in dict_consultar_pecas.items():
                    nome, fabricante, preco = item
                    if fabricante_da_peca == fabricante:
                        control += 1
                        if control == 1:
                            print('-' * 15)
                        print(f'Código: {codigo}\n'
                              f'Nome: {nome}\n'
                              f'Fabricante: {fabricante}\n'
                              f'Preço: {preco:.1f}')
                # Nesse caso utilizei ela para 2 coisas: 1ª: Caso ela tenha entrado no "If" ela vai printar para separar os items
                # 2ª: se a variável "control" for igual a "0" sinal que ela não entrou no "if" então o fabricante digitado não existe!
                if control != 0:
                    print('-' * 15)
                else:
                    print('Este fabricante não existe!')
                    continue
            elif opcao == 4:
                break
            else:
                print('Favor escolher dentre as opções abaixo: ')
                continue
        except ValueError:
            print('Favor digitar um valor númerico!')


# Função Criada para remover um item do dicionário
def removerPeca(dict_remove_pecas):
    while True:
        control = 0
        try:
            codigo_remove = int(input('Digite o código da peça a ser removida: '))
            for codigo, item in dict_remove_pecas.items():
                if codigo == codigo_remove:
                    control += 1
                    dict_remove_pecas.pop(codigo)
                    break
            if control != 0:
                break
            else:
                print('Essa peça não esta cadastrada!')
                break
        except ValueError:
            print("Favor digite um valor númerico:")


# Aqui é onde o código será executado
while True:
    try:
        opcao = int(input('Escolha a opção desejada:\n'
                          '1. Cadastrar Peça\n2. Consultar Peça\n3. Remover Peça\n4. Sair\n'))
        # Aqui é quando selecionamos a opção para cadastrar peças. Usei o format zfill(3) para criar numero com 3 casas decimais
        if opcao == 1:
            cod_peca += 1
            print(f'Você selecionou a Opção Cadastrar Peça\nCódigo da peça {str(cod_peca).zfill(3)}')
            # Usei o .update() para adicionar um item ao dicionário, como minha função já retorna um item utilizei como parametro
            dict_pecas.update(cadastrarPeca(cod_peca))
            continue
        # Aqui adicionei uma verificação do tamanho do dict, se for igual a 0 não vale a pena entrar na consulta
        # Pois não vai existir peças para consultar.
        elif opcao == 2:
            if len(dict_pecas) != 0:
                print(f'Você selecionou a Opção Consultar Peça')
                consultarPeca(dict_pecas)
                continue
            else:
                print('Nenhuma peça cadastrada!')
                continue
        elif opcao == 3:
            print(f'Você selecionou a Opção Remover Peça')
            removerPeca(dict_pecas)
            continue
        elif opcao == 4:
            break
        print('Favor escolher dentre as opções abaixo: ')
    except ValueError:
        print('Favor digitar um valor númerico!')
