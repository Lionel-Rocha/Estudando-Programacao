import datetime

def calcula_cem_anos(nome, idade):
    ano = datetime.datetime.now().year
    
    ano_nascimento = int(ano) - int(idade)
    ano_cem_anos = int(ano_nascimento) + 100
    
    print(f"Olá, {nome}, você fará cem anos em {ano_cem_anos}")

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
    
calcula_cem_anos(nome, idade)
