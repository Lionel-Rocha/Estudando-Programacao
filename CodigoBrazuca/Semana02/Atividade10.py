def primo(numero):
  if numero > 1:

      for i in range(2, (numero//2)+1):
          if (numero % i) == 0:
              return False
      else:
          return True
  else:
      return False

def main():
  n1 = int(input("Digite o 1º número do intervalo: "))
  n2 = int(input("Digite o 2º número do intervalo: "))

  for i in range (n1, n2):
    resultado = primo(i)
    if resultado:
      print(i)
    
main()
