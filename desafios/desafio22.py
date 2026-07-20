lista = ['maça', 'banana', 'melão', 'melancia', 'abaxi', 'cereja', 'uva', 'maracuja', 'manga', 'mamão']
print(f"catalogo: {lista}")

item = input("Digite a fruta que você quer: ").lower()

if item in lista:
    print("este item esta na lista boas compras!")
else:
    print("este item não esta no catalogo")