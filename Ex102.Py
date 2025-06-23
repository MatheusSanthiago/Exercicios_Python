'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
'''

def Fatorial(N, show=False):
    F = 1
    for C in range(N, 0, -1):
        if show:
            print(C, end = '')
            if C > 1:
                print(' x ', end = '')
            else:
                print(' = ', end = '')
        F *= C
    return F

help(Fatorial)