'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faca um programa que leia um ano qualquer e mostre se ele e bissexto.
'''

from datetime import date
Ano = int(input('Que ano quer analisar? Coloque o para analisar o ano atual: '))
if Ano == 0:
    Ano = date.today().year
if Ano % 4 == 0 and Ano % 100 != 0 or Ano % 400 == 0:
    print(F'O ano {Ano} e bissexto')
else:
    print(F'O ano {Ano} nao e bissexto')