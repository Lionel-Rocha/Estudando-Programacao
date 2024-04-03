def checa_palindromos(palavra):
    numero_metade = 0
    numero_metade = int(len(palavra)/2)
    
    metade_1 = palavra[:numero_metade]
    
    if (len(palavra)%2 != 0):
        metade_2 = palavra[numero_metade+1:]
    else:
        metade_2 = palavra[numero_metade:]
    
    metade_2 = metade_2[::-1] # isso reverte a string
    
    if metade_1 == metade_2:
        print("É palíndromo")
    else:
        print("Não é palíndromo")
        
palavra = input("Digite uma palavra: ")
checa_palindromos(palavra)
