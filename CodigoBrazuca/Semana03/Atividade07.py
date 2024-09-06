def calcular_media():
    total = 0
    count = 0
    while True:
        nota = float(input("Digite uma nota (-1 para sair): "))
        if nota == -1:
            break
        total += nota
        count += 1
    if count == 0:
        return 0
    return total / count

def main():
  print(f"A média das notas é {calcular_media()}.")

main()
