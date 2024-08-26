def main():
  peso = float(input("Digite seu peso: "))
  altura = float(input("Digite sua altura: "))

  imc = peso/(pow(altura, 2))

  print(f"Seu IMC é {imc}")
  
main()
