import math

def calcular_area(raio):
    return math.pi * raio ** 2

raio = float(input("Digite o valor do raio do círculo: "))
print(f"A área do círculo é {calcular_area(raio):.2f}.")
