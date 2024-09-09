def obter_numeros():
    numeros = []
    while True:
        entrada = input("Digite um número (ou 'sair' para finalizar): ")
        if entrada.lower() == 'sair':
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
    return numeros

def calcular_estatisticas(numeros):
    if not numeros:
        print("Nenhum número foi inserido.")
        return

    maior = max(numeros)
    menor = min(numeros)
    media = sum(numeros) / len(numeros)

    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")
    print(f"Média: {media:.2f}")

# Execução do programa
numeros = obter_numeros()
calcular_estatisticas(numeros)
