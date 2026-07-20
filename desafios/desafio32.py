login = "Gabriel"
senha = "1234"

for i in range(1,4):

    resposta = input("Digite o login da conta: ")
    resposta2 = input("Digite a senha da conta: ")

    if resposta == login and resposta2 == senha:
        print("Parabens você acertou")
        break
    else:
        print(f"Você errou a Tentativa {i} de 3")
        if i == 3:
            quit()

tabuada = int(input("Digite até que numero ira a tabuada: "))

for i in range(1,11):
    print(f"{tabuada} * {i} = {tabuada * i} ")