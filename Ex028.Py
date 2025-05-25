'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Escreva um programa que faca o computador "pensar" em um numero inteiro entre 0 a 5 e peca para o usuario tentar descobrir qual foi o numero escolhido pelo computador
O programa devera escrever na tela se o usuario venceu ou perdeu.
'''

from random import randint
from time import sleep
Computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um numero enmtre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
Jogador = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if Jogador == Computador:
    print('PARABNES! Voce conseguiu me vencer!')
else:
    print(F'Ganhei! eu pensei no se numero:{Computador} e nao no:{Jogador}')