nome = input("digite o seu nome de usuario: ").lower()
senha = input("Digite sua senha: ")

Rnome = input("Qual o seu nome de usuario? ").lower()
Rsenha = input("Qual a sua senha? ")

if nome == Rnome and senha == Rsenha:
    print(f"Boas vindas {nome}")
else:
    print("nome ou senha errada")