'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faca um programa que calcule a soma entre todos os numeros impares que sao multiploes de tres e que se encontram no intervalo de 1 ate 500.
'''

Soma = 0
Cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        Soma += c
        Cont += 1
print(F'A soma de todos os {Cont} valores solicitados e {Soma}')