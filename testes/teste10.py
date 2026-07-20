numero = 0

while numero == 0:
    numero = int(input("Digite um numero que não seja zero: "))

print("Fim da repetição")

while True:
    resposta = input("Degeja quebrar o loop? ").lower()

    if resposta == "sim":
        break
    elif resposta == "não":
        print("Vou continuar o loop então")
    else:
        print("Escreva uma resposta certa")