def fibonacci(quantidade):
    array = [1,1]
    for i in range (1, quantidade-1):
        soma = array[i-1]+array[i]
        array.append(soma)
    return array

print(fibonacci(4)) # printa a array inteira até o n-ésimo termo

# Extra

def fibonacci_recursivo(quantidade):
   
    if quantidade <= 1:
        return 1
    else:
        return fibonacci_recursivo(quantidade-2) + fibonacci_recursivo(quantidade-1)
    
    
print(fibonacci_recursivo(4)) # n-ésimo termo da sequência
