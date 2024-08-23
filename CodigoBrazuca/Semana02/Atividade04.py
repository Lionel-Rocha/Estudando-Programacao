def main():
  temperatura = float(input("Digite a temperatura atual: "))

  if temperatura > 30:
    print("Está quente")
  elif temperatura < 15:
    print("Está frio")
  else:
    print("Está agradável")

main()
