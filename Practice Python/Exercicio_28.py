num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
num3 = int(input("Número 3: "))

maior = 0

if (num1 > num2) and (num1 > num3):
    maior = num1
elif (num2 > num1) and (num2 > num3):
    maior = num2
else:
    maior = num3
    
print("O maior número é ", maior)

#Extra: solução para qualquer quantidade de números

def maior(*args):
    maior = float('-inf') # um número infinitamente pequeno
    for i in range(len(args)):
        if args[i] > maior:
            maior = args[i]
    
    return maior
    
print(maior(98,10,12,77,38,54,57))
