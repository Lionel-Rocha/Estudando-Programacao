import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    while True:
        palpite = int(input("Tente adivinhar o número (entre 1 e 100): "))
        if palpite < numero_secreto:
            print("Muito baixo!")
        elif palpite > numero_secreto:
            print("Muito alto!")
        else:
            print("Parabéns! Você acertou!")
            break

jogo_adivinhacao()
