# Eu usei linecache porque iterar por um arquivo desse tamanho é loucura.

import linecache
import random 

nome_arquivo = 'sowpods.txt'
numero = random.randint(1,267750)

palavra = linecache.getline('sowpods.txt', numero)

print("A palavra é: ")
print(palavra)
