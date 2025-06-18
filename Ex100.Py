'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''

from random import randint
from time import sleep

def Sorteia(lista):
    print('Sorteando 5 valores da lista: ', end = '')
    for Cont in range(0 ,5):
        N = randint(1, 10)
        lista.append(N)
        print(F'{N} ', end = '', flush = True)
        sleep(0,3)
    print('PRONTO!')
def SomaPar(lista):
    Soma = 0
    for valor in lista:
        if valor % 2 == 0:
            Soma += valor
    print(F'Somando os valores pares de {lista}, temos {Soma}')
Numeros = list()
Sorteia(Numeros)
SomaPar(Numeros)