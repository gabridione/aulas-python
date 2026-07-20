
erros = 0
resposta = "a^2 + 2ab + b^2"
pergunta = ""

print("Se quiser desistir escreva (desisto)")

while pergunta != resposta:
    pergunta = input("Quanto é o valor de (a + b)^2? se não souber escreva ")

    if pergunta == resposta:
        print("parabens você acertou!")
        print(f"Você errou {erros} vezes")
    elif pergunta == "desisto":
        print(f"A resposta era {resposta}")
        break
    else:
        print("Você errou tente novamente")
        erros = erros + 1 
