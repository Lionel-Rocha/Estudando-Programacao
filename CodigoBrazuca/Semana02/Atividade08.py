def confere_numero(numero):
  if numero % 2 == 0:
    return "par"
  else:
    return "ímpar"


def main():
  numero = int(input("Digite um número e direi se ele é par ou ímpar: "))
  resultado = confere_numero(numero)

  print("O número é", resultado)

main()
