def eh_numero_perfeito(numero):
    soma_divisores = sum([i for i in range(1, numero) if numero % i == 0])
    return soma_divisores == numero

numero = int(input("Digite um número: "))
if eh_numero_perfeito(numero):
    print(f"{numero} é um número perfeito.")
else:
    print(f"{numero} não é um número perfeito.")
