pergunta1 = int(input("Você deseja trabalhar em nossa empresa 1 para sim e 0 para não: "))

if pergunta1 == 1:
    curriculo = int(input("você trouce o seu curriculo 1 para sim e 0 para não: "))

    if curriculo == 1:
        print("Vamos começar a entrevista")
    else:
        print("infelismente não poderei fazer sua entrvista")
else:
    print("tudo bem pode ir embora")