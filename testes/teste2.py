nome = "Gabriel"
idade = 13
altura = 1.65
trabalha = False
calculo = 3*7+(5+3)

print(f"meu nome é {nome}")
print(f"minha idade é {idade}")
print(f"minha altura é {altura}")
print(f"minha situação de trabalho é {trabalha}")
print(f"3*7+(5+3)={calculo}")

nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
trabalha = input("você trabalha? sim ou não?: ")
calculo = eval(input("Digite um calculo: "))

print(f"seu nome é {nome}, sua idade è {idade}, sua altura é {altura}, você trabalha {trabalha} trabalha, o resulatado do seu calculo foi: {calculo}")