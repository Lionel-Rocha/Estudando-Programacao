def main():
  soma = 0

  entrada = int(input("Digite um número: "))

  while entrada != 0:
    soma += entrada
    entrada = int(input("Digite um número: "))

  print("Soma: ", soma)

main()
