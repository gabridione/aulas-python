def megapragiga(mega):
    giga = mega / 1024
    return giga

def metrosprakilometros(metros):
    kilo = metros / 1000
    return kilo

def celsiosprafahren(cel):
    fahren = (cel * 1.8) + 32
    return fahren

def reaispradolar(real):
    dolar = real * 0.20
    return dolar

usuario = int(input("Quais informações você precisa (Digite 1 para megabytes para gigabytes, digite 2 para metros para quitometros, digite 3 para celcios para fahrenheit ou digite 4 para reais para dolar)? "))

if usuario == 1:
    mega = int(input("Digite quantos megas: "))
    giga = megapragiga(mega)
    print(giga)
elif usuario == 2:
    metros = int(input("Digite quantos metros: "))
    kilo = metrosprakilometros(metros)
    print(kilo)
elif usuario == 3:
    cel = int(input("Digite quantos graus celsios: "))
    fahren = celsiosprafahren(cel)
    print(fahren)
elif usuario == 4:
    reais = int(input("Digite quantos reais: "))
    dolar = reaispradolar(reais)
    print(dolar)
else:
    print("!!ERROR!!")