'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faca um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao servico militar, se e a hora de se alistar ou se ja passou do tempo de alistamento. Seu programa tambem devera mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date
Atual = date.today().year
Nasc = int(input('Ano de nascimento: '))
Idade = Atual - Nasc
print(F'Quem nasceu em {Nasc} tem {Idade} em {Atual}')
if Idade == 18:
    print('Voce tem que se alistar imediatamente!')
elif Idade < 18:
    Saldo = 18 - Idade
    print(F'Ainda faltam {Saldo} para o alistamento')
    Ano = Atual + Saldo
    print('Seu alistamento sera em {Ano}')
elif Idade > 18:
    Saldo = Idade - 18
    print(F'Voce ja deveria ter se alistado ha {Saldo}')
    Ano = Atual - Saldo
    print(F'Seu alistamento foi em {Ano}')