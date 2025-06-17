'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''

from random import randint
from time import sleep
Lista = list()
Jogos = list()
print('-=' * 30)
print('     Joga na mega sena       ')
print('-=' * 30)
Quant = int(input('Quantos jogos voce quer que eu sorteie? '))
Tot = 1
while Tot <= Quant:
    Cont = 0
    while True:
        Num = randint(1, 60)
        if Num not in Lista:
            Lista.append(Num)
            Cont += 1
        if Cont >= 6:
            break
    Lista.sort()
    Jogos.append(Lista[:])
    Lista.clear()
    Tot += 1
print('-=' * 3, F'  Sorteando {Quant} jogos ', '-=' * 3)
for I, L in enumerate(Jogos):
    print(F'Jogo {I+1}: {L}')
    sleep(1)
print('-=' * 5, '< boa sorte! >', '-=' * 5)
