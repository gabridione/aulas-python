palavra = input("Digite uma frase ou palavra para eu fazer uma contagem das letras: ")

numero = 0

for i in palavra:

    numero = numero + 1

    print(f"{i} #{numero}")