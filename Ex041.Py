'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: A confedecao nacional de natacao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acodo com a idade?
Ate 9 anos: Mirim
Ate 14 anos: infantil
Ate 19 anos: Junior
Ate 25 anos Senior
Acima: Master.
'''

from datetime import date
Atual = date.today().year
Nascimento = int(input('Ano de Nascimento: '))
Idade = Atual - Nascimento
print(F'O atleta tem {Idade} anos.')
if Idade <= 9:
    print('Classificacao: Mirim')
if Idade <= 14:
    print('Classificacao: Infantil')
if Idade <= 19:
    print('Classificacao: Junior')
if Idade <= 25:
    print('Classificacao: Senior')
else:
    print('Classificacao: Master')