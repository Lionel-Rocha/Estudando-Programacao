def main():
  lista = []
  print("Digite 'sair' para sair")
  entrada = input("Digite um item: ")

  while entrada != "sair":
    lista.append(entrada)
    entrada = input("Digite um item: ")

  for item in lista:
    print(item)

main()
