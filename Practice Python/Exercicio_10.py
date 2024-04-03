from random import randint

def gera_array(tamanho):
    array = []
    for i in range(tamanho+1):
        array.append(randint(1, 100))
    return array
    
def encontra_numeros_em_comum(array1, array2):
    b = [i for i in array1 if i in array2]
    return b
        
a = gera_array(5)
b = gera_array(10)

print(a)
print(b)

print(encontra_numeros_em_comum(a,b))
