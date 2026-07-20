def convMegaGiga(mega):
    giga = mega/1024
    return giga

def convMtrsKms(metros):
    kms = metros / 1000
    return kms

def convCeFa(celsius):
    fahrenheit = (celsius *1.8) + 32
    return fahrenheit

def convRealDol(reais):
    dolar = reais * 0.19
    return dolar

print("| FERRAMENTAS DE CONVERSÕES |")
print("-"*60)

while True:
    print("| Escolha uma das Ferramentas (pelo numero) |")
    print("| 1) Megabytes > Gigabytes |")
    print("| 2) Metros > Kilometros |")
    print("| 3) Celsius > Fahrenheit |")
    print("| 4) Reais > Dolar |")
    print("| 5) Sair")
    escolha = input("Digite aqui: ")
    
    if escolha in ["1","2","3","4"]:
        valor = float(input("Digite o valor para ser convertido: "))

    if escolha == "1":
        conversao = convMegaGiga(valor)
    elif escolha == "2":
        conversao = convMtrsKms(valor)
    elif escolha == "3":
        conversao = convCeFa(valor)
    elif escolha == "4":
        conversao = convRealDol(valor)
    elif escolha == "5":
        break
    else:
        print("Não pode ser convertido! Opção incorreta!")
        conversao = 0

    print(f"O valor convertido: {conversao}")