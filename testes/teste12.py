def exibirTexto():
    print("Exibindo esse texto!")

exibirTexto()

def calcularConta():
    conta = 10+20-30*40/50**60//70
    return conta

resultado = calcularConta()
print(resultado)

def somarnumeros(num1, num2):
    resultado = num1 + num2
    print(resultado)

somarnumeros(10, 30)

def subtrairnumeros(num1, num2):
    resultado = num1 - num2
    return resultado

valor = subtrairnumeros(10, 20)
print(valor)