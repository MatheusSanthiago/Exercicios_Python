'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar ( considere US$1,00 = R$3,27).
'''

Real = float(input('Quanto dinheiro voce tem na carteira? R$ '))
Dolar = Real / 3,27
print(F'Com R${Real} voce pode comprar US${Dolar}')