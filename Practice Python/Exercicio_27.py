def inicia_array():
  array = [['_','_','_'],['_','_','_'],['_','_','_']]
  return array

def printa_tabuleiro(array):
  for linha in array:
      for elemento in linha:
          print("|", end="")
          print(elemento, end="")
          print("|", end="")
      print('\n')


def insere_simbolo(array, posicao, simbolo):
    
    x = int(posicao[0]) - 1
    y = int(posicao[1]) - 1
    
 
    array[x][y] = simbolo
    
    return array

def checa_posicao_valida(array,posicao):
    x = int(posicao[0]) - 1
    y = int(posicao[1]) - 1
    
    if array[x][y] == '_':
        return True
    else:
        return False
    
def checa_estado_jogo(array):
    for linha in array:
        for elemento in linha:
            # se houver algum elemento vazio, o jogo pode continuar
            if elemento == '_':
                return True
                
    return False
    
   

array = inicia_array()
printa_tabuleiro(array)

pode_continuar = True
vez = 1

while (pode_continuar):
    print(f"JOGADOR {vez}")
    coordenadas = input("Digite as coordenadas: ")
    posicao = coordenadas.split(",")
    movimento_valido = checa_posicao_valida(array,posicao)
    if vez == 1:
        if (movimento_valido):
            array = insere_simbolo(array, posicao, 'X')
            vez = vez + 1
        else:
            print("Movimento inválido.")
            continue
    else:
        if (movimento_valido):
            array = insere_simbolo(array, posicao, 'O')
            vez = vez - 1
        else:
            print("Movimento inválido.")
            continue
        
    printa_tabuleiro(array)
    pode_continuar = checa_estado_jogo(array)
