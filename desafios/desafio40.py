def saque(saldo, valor):
    resultado = saldo - valor
    if valor > saldo or valor < 0:
        print("!!ERROR!!")
        return saldo
    else:
        return resultado
def depositar(saldo, valor):
    resultado = saldo + valor
    if valor < 0:
        print("!!ERROR!!")
        return saldo
    else:
        return resultado

nome = input("Digite o seu nome: ")
saldo = int(input("Digite o seu saldo: "))
if saldo > 0:
    while True:
        print(f"o seu saldo é de {saldo} reais")
        print("Escolha pelo numero:")
        print("1) sacar \n2) depositar \n3) sair")
        escolha = int(input("O que você pretende fazer: "))

        if escolha == 1:
            valor = int(input("Quantos reais você vai sacar? "))
            saldo = saque(saldo, valor)
        elif escolha == 2:
            valor = int(input("Digite quanto você quer depositar: "))
            saldo = depositar(saldo, valor)
        elif escolha == 3:
            print(f"Até mais {nome}")
            break
        else:
            print("!!ERROR!!")          
else:
    print("!!ERROR!!")