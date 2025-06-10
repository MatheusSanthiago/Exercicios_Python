'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Desenvolva um programa que leia o primeiro termo e a razao de uma pa no final, mostre os 10 primeiros termos dessa progressao.
'''

Primeiro = int(input('Primeiro termo: '))
Razao = int(input('Razao: '))
Decimo = Primeiro + (10 - 1) * Razao
for C in range(Primeiro, Decimo + Razao, Razao):
    print(F'{C}')
print('Acabou')