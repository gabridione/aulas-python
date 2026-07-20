listaf = ['João', 'Gabriel', 'Pedro', 'Erick', 'Murilo', 'Anita', 'Ana', 'Gabriela', 'Amanda', 'Agata']
listab = ['João', 'Gabriel', 'Ana', 'Gabriela']

nome = input ("qual o seu nome? ").capitalize()

if nome in listaf:
    if nome not in listab:
        print(f"Pode entrar {nome} você esta na lista de funcionarios,\ne não esta na lista dos banidos")
    else:
        print(f"{nome} você esta na lista de banidos da festa,\ne por isto não podera entrar")
else:
    print(f"Pelo visto {nome} você não é um funcionario da impresa")