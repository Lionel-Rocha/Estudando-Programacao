#Usei recursão porque sabia a resolução desse exercício de "vidas passadas"

def fatorial(numero):
    if numero == 0:
      return 1
    else:
      return numero * fatorial(numero - 1) 

def main():
  numero = int(input("Digite um número: "))
  fat_numero = fatorial(numero)

  print(f"O fatorial do número {numero} é {fat_numero}")

main()
