def tabuada():
    tabuada = int(input("Digite até que numero ira a tabuada: "))

    for i in range(1,11):
        print(f"{tabuada} * {i} = {tabuada * i} ")

def maquinadasorte():
    import random

    lista = ["100", "10", "1.000", "10.000", "10", "100", "10", "10", "100", "1.000"]

    for i in range(1, 4):
        print(f"Tentativa numero {i}")
    
        valor = random.choice(lista)

        if valor == "10.000":
            print(f"parabens você ganhou: R${valor},00 o maior premio")
            break

        print(f"O resultado da {i}º tentativa é de: R${valor},00")
    
        if i != 3:
            pergunta = input("Você quer tentar novamente (responda com sim ou não)? ")
        else:
            print("Está foi a sua ultima tentativa")
            break

        if pergunta == "não":
            break

def dados():
    import random
    lados = int(input("Digite quantos lados você quer que tenha no seu dado: "))

    while True:
        pergunta = input("Você quer girar o dado (responda com sim ou não)? ").lower()

        if pergunta == "sim":
            valor = random.randint(1,lados)
            print(f"O valor do dado foi: {valor}")
        else:
            break

while True:

    denovo = input("Você quer jogar (sim ou não)? ")

    if denovo == "sim":

        escolha = input("Você tem três opções de jogos (dados, maquina da sorte e a tabuada), qual você vai escolher? ")

        if escolha == "dados":
            dados()
        elif escolha == "maquina da sorte":
            maquinadasorte()
        elif escolha == "tabuada":
            tabuada()
        else:
            print("!ERRO!")
    else:
        break