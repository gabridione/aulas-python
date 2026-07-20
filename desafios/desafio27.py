numero = int(input("Digite quantas repetições: "))

for i in range(2,numero + 1, 2):
    print(f"#{i}")

print("-"*30)

for i in range(1,numero + 1, 2):
    print(f"#{i}")