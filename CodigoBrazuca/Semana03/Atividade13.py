def somar_pares():
    soma = 0
    for numero in range(2, 101, 2):
        soma += numero
    return soma

print(f"A soma dos números pares entre 1 e 100 é {somar_pares()}.")
