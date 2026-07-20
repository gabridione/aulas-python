senha = int(input("digite a senha: "))

senha1 = 29

if senha == senha1:
    print("correto esta era a senha")
else:
    print("esta não era a senha")
    if senha < senha1:
        print("sua tentativa foi menor do que a senha")
    else:
        print("sua tentativa foi maior do que a senha")