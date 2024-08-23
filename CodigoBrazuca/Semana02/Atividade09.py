def confere_caracter(string):
  contador = 0
  for i in range (len(string)):
    if string[i] == 'a':
      contador += 1

  return contador

def main():
  string = input("Digite uma frase e direi quantas vezes a letra A aparece: ")
  resultado = confere_caracter(string)

  print(f"O caracter A apareceu {resultado} vezes")

main()
