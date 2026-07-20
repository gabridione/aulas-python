lista = ["uranio", "maçã", "paracetamol", "rifle", "jacaré", "petroleo"]

acertos = 0

for i in lista:

    print(i)

    palavras = input("Digite corretamente as palavras da lista: ")

    if palavras == i:
        print("você acertou párabens")
        acertos = acertos + 1
    else:
        print("você errou")

print(f"Você acertou {acertos} palavras")