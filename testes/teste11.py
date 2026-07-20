import math

num1 = 400
num2 = 35
divisao = num1 / num2
arredondado = math.floor(divisao)
raizQuadrada = math.sqrt(num1)
pi = math.pi

print(f"Divisão: {divisao} | Arredondado: {arredondado}")
print(f"Raiz Quadrada: {raizQuadrada} | Pi: {pi}")

import random

valor = random.randint(1,100)
print(f"Valor aleatorio: {valor}")

lista = ["a","b","c","d","e","f"]
itemAleatorio = random.choice(lista)
print(f"Item escolhido: {itemAleatorio}")