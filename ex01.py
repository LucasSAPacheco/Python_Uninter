print("Bem vindo a loja do Lucas Santana de Amorim Pacheco")
valor_unitario = float(input("Digite o valor unitário do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

# Aqui estamos calculando o valor total a ser pago pelo cliente sem desconto.
valor_total_sem_desconto = valor_unitario * quantidade

if quantidade >= 1000:
    desconto = 0.15 # 15% de desconto para compras com mais de 1000 unidades
elif quantidade >= 10:
    desconto = 0.1  # 10% de desconto para compras de 10 até 999 unidades
elif quantidade >= 5:
    desconto = 0.05  # 5% de desconto para compras de 5 até 9 unidades
else:
    desconto = 0  # Compras abaixo de 5 uninades não irão receber descontos


# O valor total com descontos nada mais é do que o valor total menos o valor sem desconto vezes o desconto
valor_total_com_desconto = valor_total_sem_desconto - (valor_total_sem_desconto * desconto)

print(f"Valor total sem desconto: {valor_total_sem_desconto:.2f}")
print(f"Valor total com desconto: {valor_total_com_desconto:.2f}  ({desconto * 100}% de desconto)")
