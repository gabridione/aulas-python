lista = ["maçã", "banana", "uva", "abacaxi", "melão", "manga", "limão"]

for i in lista:
    print(i)
    resposta = input("Você quer comprar este produto (Responda com sim ou não): ").lower()

    if resposta == "sim":
        print(f"Você escolheu {i}")
        break

if resposta == "sim":
    print("Tenha um otimo dia")   
else:
    print("Você não escolheu nenhum produto")
