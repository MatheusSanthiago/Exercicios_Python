'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada.
'''

from time import sleep
def contador(I, F, P):
    print('-=' * 20)
    print(F'Contagem de {I} ate {F} de {P} em {P}')
    sleep(2.5)
    if I < F:
        Cont = I
        while Cont <= F:
            print(F'{Cont}', end = '', flush = True)
            sleep(0,5)
            Cont += P
        print('Fim')
    else:
        Cont = I
        while Cont <= F:
            print(F'{Cont}', end = '', flush = True)
            sleep(0,5)
            Cont -= P
        print('Fim')
    print('-=' * 20)

contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora e sua vez de personalizar a contagem!')
Ini = int(input('Inicio: '))
Fim = int(input('Fim: '))
Pas = int(input('Passo: '))
contador(Ini, Fim, Pas)