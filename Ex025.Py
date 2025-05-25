'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''

Nome = str(input('Qual e seu nome completo? ')).strip
print('Seu nome tem silva? {}'.format('silva' in Nome.lower()))