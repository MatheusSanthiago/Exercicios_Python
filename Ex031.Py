'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preco da passagem, cobrando R$0,50= por Km para viagens de ate 200Km e R$0,45 para viagens mais longas.
'''

Distancia = float(input('Qual e a distancia da sua viagem? '))
print(F'Voce esta prestes a comecar uma viagem de {Distancia}Km')
Preco = Distancia * 0.50 if Distancia <= 200 else Distancia * 0,45
print(F'E o preco da sua passagem sera de R${Preco}')