# Função criada para retornar o volume do objeto
def dimensoesObjeto():
    while True:
        try:
            altura = float(input("Digite a altura do objeto (em cm): "))
            comprimento = float(input("Digite o comprimento do objeto (em cm): "))
            largura = float(input("Digite a largura do objeto (em cm): "))
            print(f'O volume do objeto é (em cm³): {altura * comprimento * largura:.1f}')
            if altura * comprimento * largura < 100000:
                return altura * comprimento * largura
            print("Não aceitamos objetos tão grandes!")
        except ValueError:
            print("Valor inválido. Por favor, digite um valor numérico.")


# Função criada para retornar o peso do objeto
def pesoObjeto():
    while True:
        try:
            peso = float(input("Digite o peso do objeto (em kg): "))
            if peso < 30:
                return peso
            print('Não aceitamos objetos tão pesados')
        except ValueError:
            print("Valor inválido. Por favor, digite um valor numérico.")


# Função criada para retornar o multiplicador que irá servir para multiplicar no valor final
def rotaObjeto():
    rotas = [('RS', 'De Rio de Janeiro até São Paulo', 1),
                ('SB', 'De São Paulo até Brasília', 1.2),
                ('RB', 'De Rio de Janeiro até Brasília', 1.5)]

    print('Selecione a rota: ')
    for sigla, destino, multiplicador in rotas:
        print(sigla, '-', destino)
    while True:
        rota = input("Digite a Rota que você deseja: ").upper()
        for item in rotas:
            if rota == item[0]:
                return item[2]
        else:
            print('Rota inválida. Por favor, digite uma rota valida')


print('Bem vindo a Transportadora do Lucas Santana de Amorim Pacheco')
# Essas são as 3 variáveis criadas para armazenar o valor de cada função.
volume = dimensoesObjeto()
peso = pesoObjeto()
mult_rota = rotaObjeto()

# Essas 3 variáveis foram criadas para salvar os valores que irão ser usado para o calculo do valor final.
valor = 0.0
mult_peso = 0.0
valor_vol = 0.0

# Aqui setamos o valor que será pago e salvamos o valor inicial selecionado para o "print" final
if volume < 1000:
    valor = 10.0
    valor_vol = 10.0
elif volume < 10000:
    valor = 20.0
    valor_vol = 20.00
elif volume < 30000:
    valor = 30.0
    valor_vol = 30.0
elif volume < 100000:
    valor = 50.0
    valor_vol = 50.0

if peso <= 0.1:
    valor *= 1
    mult_peso = 1
elif peso < 1:
    valor *= 1.5
    mult_peso = 1.5
elif peso < 10:
    valor *= 2
    mult_peso = 2
elif peso < 30:
    valor *= 3
    mult_peso = 3

valor *= mult_rota

print(f"Total a pagar (R$): {valor:.2f} (Dimensões: {valor_vol} * peso: {mult_peso} * rota: {mult_rota})")