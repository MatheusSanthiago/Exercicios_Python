'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

from random import randint
while True:
    Jogador = int(input('Diga um valor: '))
    Computador = randint(0, 10)
    Total = Jogador + Computador
    Tipo = ' '
    while Tipo not in 'PI':
        Tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(F'Voce jogou {Jogador} e o computador {Total}')
    print('Deu par' if Total % 2 == 0 else 'Deu Impar')
    if Tipo == 'P':
        if Total % 2 == 0:
            print('Voce Venceu!')
            V += 1
        else:
            print('Voce perdeu!')
            break
    elif Tipo == 'I':
        if Total % 2 == 1:
            print('Voce venceu!')
            V += 1
        else:
            print('Voce perdeu!')
            break
    print("Vamos jogar novamente...")