def contar_palavras(frase):
    return len(frase.split())

frase = input("Digite uma frase: ")
print(f"A frase contém {contar_palavras(frase)} palavras.")
