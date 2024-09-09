def calcular_media_ponderada(nota1, nota2, nota3):
    return (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10

nota1 = float(input("Digite a primeira nota (peso 2): "))
nota2 = float(input("Digite a segunda nota (peso 3): "))
nota3 = float(input("Digite a terceira nota (peso 5): "))

print(f"A média ponderada é {calcular_media_ponderada(nota1, nota2, nota3):.2f}")
