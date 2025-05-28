'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faca um programa que leia tres numeros e mostre qual e o maior e qual e o menor.
'''

A = int(input('Primeiro valor: '))
B = int(input('Segundo valor: '))
C = int(input('Terceiro valor: '))
# Verificando quem e menor
Menor = A
if B < A and B < C:
    Menor = B
if C < A and C < B:
    Menor = C
# Verificando queme e maior
Maior = A
if B > A and B > C:
    Maior = B
if C > A and C > B:
    Maior = C
print(F'O menor valor digitado foi {Menor}')
print(F'O maior valor digitado foi {Maior}')