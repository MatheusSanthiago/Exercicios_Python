'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que faca o computador jogar jokenpo com voce.
'''

from random import randint
Itens = ('Pedra', 'Papel', 'Tesoura')
Computador = randint(0, 2)
print('''
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')
jogador = int(input('Qual e a sua jogada? '))
print('-=' * 11)
print(F'Computador jogou {Itens[Computador]}')
print(F'Jogador jogou {Itens[jogador]}')
print('-=' * 11)

if Computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador venceu')
    elif jogador == 2:
        print('Computador venceu')
    else:
        print('Jogada invalida!')

elif  Computador == 1:
    if jogador == 0:
        print('Computador venceu')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador venceu')
    else:
        print('Jogada invalida!')

elif  Computador == 2:
    if jogador == 0:
        print('Jogador venceu')
    elif jogador == 1:
        print('Computador venceu')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada invalida!')