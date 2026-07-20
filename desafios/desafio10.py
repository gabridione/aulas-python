preco1 = float(input("Digite um preço: "))
preco2 = float(input("Digite outro preço: "))
preco3 = float(input("Digite outro preço: "))

total = preco1 + preco2 + preco3

vista = total - ((total / 100) * 5)
credito = ((total / 100) * 7.5) + total

print(f"o valor total da sua compra é {total}R$ mas se pagar no crédito ficara {credito}R$ se pagar á vista ficara {vista}R$ se pagar nno debito mantera o valor de {total}R$")