import random

def adivinhe(x):
    numero_aleatorio = random.randint(1,x)
    palpite = 0
    while palpite != numero_aleatorio:
        palpite = int(input(f'Dê seu palpite entre 1 e {x}: '))
        if palpite < numero_aleatorio:
            print('Tente um número maior!')
        elif palpite > numero_aleatorio:
            print('Tente um número menor!')
    print(f'Parabéns, você acertou, o número era {numero_aleatorio}!')

x = int(input(f'Deseja gerar um número de 1 até: '))

adivinhe(x)
