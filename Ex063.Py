'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
'''

print('-' * 30)
print('Sequencia de fibonacci')
print('-' * 30)
N = int(input('Quantos termos voce quer mostrar? '))
T1 = 0
T2 = 1
print('~' * 30)
print(F'{T1} - {T2}')
Cont = 3
while Cont <= N:
    T3 = T1 + T2
    print(F' - {T3}')
    T1 = T2
    T2 = T3
    Cont += 1
print(' - Fim')
print('~' * 30)