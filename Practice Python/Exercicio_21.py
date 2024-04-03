nome_arquivo = input("Qual será o nome do arquivo? ")
texto_arquivo = "Algum texto bem legal"

nome_arquivo = nome_arquivo + ".txt"

with open(nome_arquivo, 'w') as open_file:
    open_file.write(texto_arquivo)
