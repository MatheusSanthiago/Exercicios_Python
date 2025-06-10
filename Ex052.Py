'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faca um programa que leia um numero inteiro e diga se ele e ou nao um numero primo.
'''

Num = int(input('Digite um numero: '))
Tot = 0
for C in range(1, Num + 1):
    if Num % C == 0:
        print('\033[33m]')
    else:
        print('\033[31m]')
print(F'\n\033[mo numero {Num} foi divisivel {Tot} vezes]')
if Tot == 2:
    print('E por isso ele e primo!')
else:
    print('E por isso ele nao e primo!')