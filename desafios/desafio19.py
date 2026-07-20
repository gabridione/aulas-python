pontos = int(input("Digite a sua pontuação: "))

if pontos > 0 and pontos <= 200:
    print("O seu rank foi iniciante")
elif pontos >= 201 and pontos <= 500:
    print("O seu rank foi veterano")
elif pontos >= 501 and pontos <= 700:
    print("O seu rank foi mestre")
elif pontos >= 701 and pontos <= 1000:
    print("O seu rank foi lendario")
elif pontos > 1000:
    print("O seu rank foi campeão")