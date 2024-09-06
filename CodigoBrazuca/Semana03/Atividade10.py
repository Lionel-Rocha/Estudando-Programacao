def verificar_paridade(numero):
    return "par" if numero % 2 == 0 else "ímpar"

numero = int(input("Digite um número inteiro: "))
print(f"O número {numero} é {verificar_paridade(numero)}.")
