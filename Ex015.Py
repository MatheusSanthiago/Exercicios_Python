'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preco a pagar, 
sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

Dias = int(input('Quantos dias alugados? '))
Km = float(input('Quantos Km rodados? '))
Pago = (Dias * 60) + (Km * 0.15)
print(f'O total a pagar e de R${Pago}')