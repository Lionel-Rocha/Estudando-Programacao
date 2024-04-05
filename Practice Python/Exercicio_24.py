def imprime_quadro(altura, largura):
    for i in range(altura):
        for i in range(largura): 
            print("|",end="")
            print("___",end="")
            print("|",end="")
        print("\n")
        

imprime_quadro(3,3)
