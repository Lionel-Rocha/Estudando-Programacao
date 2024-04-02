import datetime

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

ano = datetime.datetime.now().year

ano_nascimento = int(ano) - int(idade)
ano_cem_anos = int(ano_nascimento) + 100

print(f"Olá {nome}, você fará cem anos em {ano_cem_anos}")

#Extras

vezes = input("Quantas vezes você quer repetir essa frase? ")
print("\n")
for i in range (int(vezes)):
  print(f"Olá {nome}, você fará cem anos em {ano_cem_anos}")
  print("\n")