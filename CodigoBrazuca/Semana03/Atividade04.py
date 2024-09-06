def palindromo(string_original):
  string_original = string_original.replace(' ', '') #para tirar os espaços da frase
  string_palindromo = string_original[::-1] #achei esse macete no w3schools
  
  for i in range (len(string_original)):
    if string_palindromo[i] != string_original[i]:
      return False

  return True


def main():
  string_original = input("Digite uma palavra/frase: ")
  eh_palindromo = palindromo(string_original)
  print(eh_palindromo)


main()
