'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faca um algoritimo que leia o preco de um produto e mostre seu novo preco, com 5% de desconto.
'''

Preco = float(input('Qua; e o preco do produto? R$ '))
Novo = Preco - (Preco * 5 / 100)
print(F'O produto que custava R${Preco}, na promocao com desconto de 5% vai custar R${Novo}')