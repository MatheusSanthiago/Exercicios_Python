'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com o nome "SANTO".
'''

Cid = str(input('Em que cidade voce nasceu: ')).strip()
print(Cid[:5].upper() == "SANTO")