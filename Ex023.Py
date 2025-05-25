'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
'''

Num = int(input('Informe um numero: '))
U = Num // 1 % 10
D = Num // 10 % 10
C = Num // 100 % 10
M = Num // 1000 % 10
print(F'Analisando o numero {Num}')
print(F'Unidade: {U}')
print(F'Dezena: {D}')
print(F'Centena: {C}')
print(F'Milhar: {M}')