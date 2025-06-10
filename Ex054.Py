'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''

from datetime import date
Atual = date.today().year
TotMaior = 0
TotMenor = 0
for Pess in range(1, 8):
    Nasc = int(input(F'Em que ano a {Pess} pessoa nasceu? ' ))
    Idade = Atual - Nasc
    if Idade >= 21:
        TotMaior += 1
    else:
        TotMenor += 1
print(F'Ao todo tivemos {TotMaior} pessoas maiores de idade')
print(F'Ao todo tivemos {TotMenor} pessoas menores de idade')