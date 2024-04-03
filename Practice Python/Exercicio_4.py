def calcula_divisores(numero):
    array_divisores = []
    for i in range (1, numero+1):
        if (numero % i == 0):
            array_divisores.append(i)
    
    return array_divisores
    
numero = int(input("Digite um número: "))
divisores = calcula_divisores(numero)
print(f"Os divisores do número {numero} são: ", divisores)
