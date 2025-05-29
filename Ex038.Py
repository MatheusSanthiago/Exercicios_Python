'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor e maior
- O segundo valor e maior
- Nao existe valor maior, os dois sao iquais.
'''

N1 = int(input('Primeiro numero: '))
N2 = int(input('Segundo numero: '))
if N1 > N2:
    print('O primeiro valor e maior')
elif N2 > N1:
    print('O segundo valor e maior')
else:
    print('Os dois valores sao iquais')