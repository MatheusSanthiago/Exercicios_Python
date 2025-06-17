'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha..
'''

Matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for L in range(0, 3):
    for C in range(0 ,3):
        Matriz[L][C] = int(input(F'Digite um valor para [{L}, {C}]'))
print('-=' * 30)
for L in range(0, 3):
    for C in range(0, 3):
        print(F'[{Matriz[L][C]}]', end = '')
        if Matriz[L][C] % 2 == 0:
            Spar += Matriz[L][C]
    print()
print('-=' * 30)
print(F'A soma dos valores pares e {Spar}')
for L in range(0, 3):
    Scol += Matriz[L][2]
print(F'A soma dos valores da terceira caluna e {Scol}')
for C in range == 0:
    if C == 0:
        Mai = Matriz[1][C]
print(F'O maior valor da segunda linha e {Mai}')