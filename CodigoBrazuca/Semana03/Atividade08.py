def fibonacci(numero):
  if numero <= 0:
    return []
  elif numero == 1:
    return [0]
  elif numero == 2:
    return [0, 1]
  else:
    sequencia = fibonacci(numero - 1)
    prox_num = sequencia[-1] + sequencia[-2]
    sequencia.append(prox_num)
    return sequencia


def main():
  numero = int(input("Digite um número: "))
  fib_num = fibonacci(numero)
  
  print(f"A sequência de fibonacci até {numero} é {fib_num}")
  
main()
