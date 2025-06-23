'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''

def voto(Ano):
    from datetime import date
    Atual = date.today().year
    Idade = Atual - Ano
    if Idade < 16:
        return f'Com {Idade} anos: nao vota.'
    elif 16 <= Idade < 18 or Idade > 65:
        return f'Com {Idade} anos: voto opcional.'
    else:
        return f'Com {Idade} anos: voto obrigatorio.'

Nasc = int(input('Em que ano voce nasceu? '))
print(voto(Nasc))