nome = input("Digite o seu nome: ")
convite = input("Você tem um convite (responda com 'sim' ou 'não'): ").lower()
idade = int(input("Digite sua idade: "))

if convite == 'sim':
    if idade >= 21:
        print(f"Sejá bem vindo a festa {nome}")
    else:
        print(f"Pelo visto sua idade é inferior a idade minima da festa então você não podera entrar {nome}")
elif idade >= 21:
    print(f"Pelo visto você não tem um convite então infelizmente você não podera entrar na festa {nome}")
else:
    print(f"Você não possui a idade minima e também não possui um convite então você não podera entrar na festa {nome}")