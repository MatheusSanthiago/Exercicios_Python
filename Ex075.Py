'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''

Num = (int(input('Digite um numero:')), int(input('Digite outro numero: ')), int(input('Digite mais um numero: ')), int(input('Digite o ultimo numero: ')))
print(F'Voce digitou os valores {Num}')
print(F'O valor 9 apareceu {Num.count(9)} Vezes')
if 3 in Num:
    print(F'O valor 3 apareceu na {Num.index(3)+1} posicao')
else:
    print('O valor 3 nao foi digitado em nenhuma posicao')
print('Os valores pares digitados foram: ')
for N in Num:
    if N % 2 == 0:
        print(N)