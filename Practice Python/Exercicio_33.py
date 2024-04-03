dicionario_aniversarios = {
  "Madonna":"16 de agosto",
  "Elton John":"25 de março",
  "Damon Albarn":"23 de março"
}

print("O dicionário tem as datas de aniversário de: ")

for nome in dicionario_aniversarios.keys():
  print(nome)

# Também pode ser o seguinte:
# for nome in dicionario_aniversarios:
#   print(nome)

nome = input("Digite o nome de quem você deseja saber a data de aniversário: ")

if nome in dicionario_aniversarios:
  print("O aniversário de", nome, "é em", dicionario_aniversarios[nome])
else:
  print("Não está no dicionário de aniversários")
