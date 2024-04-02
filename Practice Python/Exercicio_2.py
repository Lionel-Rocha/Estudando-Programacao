numero = int(input("Digite um número: "))

if (numero % 2 == 0):
  print("O número é par")
else:
  print("O número é ímpar")

# Extras 

if (numero % 4 == 0):
  print("O número é divisível por 4")
  
else:
  print("Nenhuma das condições foi alcançada.")

dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

if (dividendo % divisor == 0):
  print(f"{dividendo} é divisível por {divisor}")
else:
  print(f"{dividendo} não é divisível por {divisor}")
