sobra = int(input("Digite o quanto de litros de gasolina esta sobrando: "))
quantia = int(input("Digite quanto em litros de gasolina você quer: "))

if quantia <= sobra:
    print("você abasteceu com sucesso")
else:
    print("você não conseguiu abastecer")