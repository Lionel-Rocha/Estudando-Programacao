nome_arquivo = "nomes.txt"
dicionario_nomes = {}

with open(nome_arquivo, "r") as open_file:
  linha = open_file.readline()
  
  while linha:
    linha = linha.strip() # para remover o \n
    if linha not in dicionario_nomes:
      dicionario_nomes[linha] = 1
    else:
      dicionario_nomes[linha] += 1
    
    linha = open_file.readline()

print(dicionario_nomes)
