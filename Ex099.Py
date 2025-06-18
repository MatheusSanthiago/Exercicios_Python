'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
from time import sleep

def Maior(* Num):
    Cont = Maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for Valor in Num:
        print(F'{Valor} ', end = '', flush = True)
        sleep(0.3)
        if Cont == 0:
            Maior = Valor
        else:
            if Valor > Maior:
                Maior = Valor
        Cont += 1
    print(F'Foram informados {Cont} Valores ao todo.')
    print(F'O maior valor informado foi {Maior}')

Maior(2, 9, 4, 5, 7, 1)
Maior(4, 7, 0)
Maior(1, 2)
Maior(6)
Maior()