'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Escreva um programa que leia a velocidade de um carro se ele ultrapassar 80Km, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km
acima do limite.
'''

Velocidade = float(input('Qual e a velocidade atual do carro? '))
if  Velocidade > 80:
    print('MULTADO! Voce excedeu o limite permitido que e de 90Km/h')
    Multa = (Velocidade - 80) * 7
    print(F'Voce deve pagar uma multa de R${Multa}')
print('Tenha um bom dia! Dirija com seguranca!')