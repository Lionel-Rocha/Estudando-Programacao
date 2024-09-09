def soma_n_numeros(n):
    return sum(range(1, n+1))

n = int(input("Digite um número: "))
print(f"A soma dos {n} primeiros números é {soma_n_numeros(n)}.")
