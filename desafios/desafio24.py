numero1 = float(input("Digite o primeiro numero do calculo: "))
numero2 = float(input("Digite o segundo numero do calculo: "))
operador = input("Digite qual operador você ira usar(+,-,*,/,**): ")

 

if operador == '+':
    resultado = numero1 + numero2
elif operador == '-':
    resultado = numero1 - numero2
elif operador == '*':
    resultado = numero1 * numero2
elif operador == '/':
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "NULO"
elif operador == '**':
    resultado = numero1 ** numero2

if operador == '+' or operador == '-' or operador == '*' or operador == '/' or operador == '**':
    print(f"{numero1} {operador} {numero2} = {resultado}")
else:
    print("ERROR")