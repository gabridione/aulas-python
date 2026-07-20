import random
lados = int(input("Digite quantos lados voê quer que tenha no seu dado: "))

while True:
    pergunta = input("Você quer girar o dado (responda com sim ou não)? ").lower()

    if pergunta == "sim":
        valor = random.randint(1,lados)
        print(f"O valor do dado foi: {valor}")
    else:
        break
