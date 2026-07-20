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