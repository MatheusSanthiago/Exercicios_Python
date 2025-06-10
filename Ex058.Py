'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''

from random import randint
Computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
print('Sera que voce conseque adivinhar qual foi? ')
Acertou = False
Palpites = 0
while not Acertou:
    Jogador = int(input('Qual e seu palpite? '))
    Palpites += 1
    if Jogador == Computador:
        Acertou = True
    else:
        if Jogador < Computador:
            print('Mais... Tente mais uma vez.')
        elif Jogador > Computador:
            print('Menos... Tente mais uma vez.')
print(F'Acertou com {Palpites} Tentativas. PARABENS!')