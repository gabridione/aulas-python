numero1 = int(input("Digite o primero numero da adição: "))
numero2 = int(input("Digite o segundo numero da adição: "))

resultado = numero1 + numero2

print(f"O resultado foi {resultado}")

if resultado > 0:
    print("Seu numero é positivo")
else:
    if resultado == 0:
        print("resultado neutro")
    else:
        print("Seu numero é negativo")