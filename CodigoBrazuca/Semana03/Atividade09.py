def ordenar_numeros(a, b, c):
    return sorted([a, b, c])
    #Pode ser feito com 3 variáveis e ifs.

def main():
  num1 = float(input("Digite o primeiro número: "))
  num2 = float(input("Digite o segundo número: "))
  num3 = float(input("Digite o terceiro número: "))
  
  ordenados = ordenar_numeros(num1, num2, num3)
  print(f"Os números em ordem crescente são: {ordenados}")

main()
