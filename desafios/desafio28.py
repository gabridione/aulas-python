soma = int(input("Digite quantos numeros você quer somar: "))

resultado = 0
conta = ""

for i in range(1,soma + 1):
    numero = int(input(f"Digite o {i}# numero: "))
    resultado = numero + resultado
    conta = conta + str(numero)
    if i < soma:
        conta = conta + "+"


print(f"Resultado da soma: {conta} = {resultado}")