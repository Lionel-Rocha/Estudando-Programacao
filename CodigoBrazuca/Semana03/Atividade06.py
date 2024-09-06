def contar_vogais(frase):
    vogais = 'aeiouAEIOU'
    contagem = 0
    for letra in frase:
        if letra in vogais:
            contagem += 1
    return contagem

def main():
  frase = input("Digite uma frase: ")
  print(f"A frase contém {contar_vogais(frase)} vogais.")
