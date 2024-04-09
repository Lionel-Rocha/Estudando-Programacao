# horizontal: para cada linha, verificar se [i][0], [i][1] e [i][2] são iguais

# vertical: para cada coluna, verificar se [0][i],[1][i] e [2][i] são iguais

# diagonal \ : verificar se [0][0],[1][1] e [2][2] são iguais

#diagonal /: verificar se [2][0], [1][1] e [0][2] são iguais

def verifica_horizontal(array):
    for i in range (3):
        if array[i][0] == array[i][1] and array[i][1] == array[i][2]:
            if array[i][0] == 1:
                return 1
            elif array[i][0] == 2:
                return 2
                
    return 0
    
def verifica_vertical(array):
    for i in range(3):
        if array[0][i] == array[1][i] and array[1][i] == array[2][i]:
            if array[0][i] == 1:
                return 1
            elif array[i][0] == 2:
                return 2
                
    return 0
    
def verifica_diagonal_igual(array):
    if array[0][0] == array[1][1] and array[1][1] == array[2][2]:
        if array[0][0] == 1:
            return 1
        elif array[0][0] == 2:
            return 2
    
    return 0
    
def verifica_diagonal_diferente(array):
    if array[2][0] == array[1][1] and array[0][2] == array[1][1]:
        if array[2][0] == 1:
            return 1
        elif array[2][0] == 2:
            return 2
    
    return 0

def verifica_vencedor(array):
    horizontal = verifica_horizontal(array)
    vertical = verifica_vertical(array)
    diagonal_iguais = verifica_diagonal_igual(array)
    diagonal_diferentes = verifica_diagonal_diferente(array)
    
    if vertical > horizontal and vertical > diagonal_iguais and vertical > diagonal_diferentes:
        return vertical
    elif horizontal > vertical and horizontal > diagonal_iguais and horizontal > diagonal_diferentes:
        return horizontal
    elif diagonal_iguais > horizontal and diagonal_iguais > vertical and diagonal_iguais > diagonal_diferentes:
        return diagonal_iguais
    elif diagonal_diferentes > horizontal and diagonal_diferentes > vertical and diagonal_diferentes > diagonal_iguais:
        return diagonal_diferentes
    else:
        return 0
    

vencedor = float("-inf")
sem_vencedor = [[2, 0, 2],
	[2, 1, 0],
	[1, 0, 1]]
	

vencedor = verifica_vencedor(sem_vencedor)

print(vencedor)
