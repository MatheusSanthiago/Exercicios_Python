'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''

Maior = 0
Menor = 0
for P in range(1, 6):
    Peso = float(input(F'Peso da {P} pessoa'))
    if P == 1:
        Maior = Peso
        Menor = Peso
    else:
        if Peso > Maior:
            Maior = Peso
        if Peso < Menor:
            Menor = Peso
print(F'O maior peso lido foi de {Maior}Kg')
print(F'O menor peso lido foi de {Menor}Kg')