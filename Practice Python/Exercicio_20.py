a = [1,2,3,4,5,6,7,8,9,10]
numero = int(input("Digite um número: "))

existe = False

if (numero > a[int(len(a)/2)]):
    for i in range (int(len(a)/2), len(a)):
        if (a[i] == numero):
            existe = True
else:
    for i in range (a[int(len(a)/2)], 0, -1):
        if (a[i] == numero):
            existe = True
            
print(existe)
