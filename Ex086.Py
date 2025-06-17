'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
'''

Matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for L in range(0, 3):
    for C in range(0 ,3):
        Matriz[L][C] = int(input(F'Digite um valor para [{L}, {C}]'))
print('-=' * 30)
for L in range(0, 3):
    for C in range(0, 3):
        print(F'[{Matriz[L][C]}]', end = '')
    print()