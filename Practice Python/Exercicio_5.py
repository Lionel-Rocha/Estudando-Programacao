from random import randint

def gera_array(tamanho):
    array = []
    for i in range(tamanho+1):
        array.append(randint(1, 100))
    return array
    
def encontra_numeros_em_comum(array1, array2):
    array_comum = []
    for elemento in array2:
        if elemento in array1:
            array_comum.append(elemento)
    return array_comum
        
a = gera_array(5)
b = gera_array(10)

print(a)
print(b)

array_comum = encontra_numeros_em_comum(a,b)
print(array_comum)
