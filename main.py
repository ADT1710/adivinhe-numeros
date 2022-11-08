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

# x = int(input(f'Deseja gerar um número de 1 até: '))

def computador_advinhara(x):
    menor = 1
    maior = x
    resposta = ''

    while resposta != "c":
        palpite = random.randint(menor, maior)
        resposta = input(f'O palpite {palpite} está muito alto (A), muito baixo (B) ou está correto (C)? R: ').lower()

        if resposta == 'a':
            maior = palpite - 1

        elif resposta == 'b':
            menor = palpite + 1

    print(f'O computador deu o palpite correto que é {palpite}')

computador_advinhara(1001)
