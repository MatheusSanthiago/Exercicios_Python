'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

from datetime import datetime
Dados = dict()
Dados['Nome'] = str(input('Nome: '))
Nasc = int(input('Ano de Nascimento: '))
Dados['Idade'] = datetime.now().year - Nasc
Dados['Ctps'] = int(input('Carteira de trabalho (0 nao tem): '))
if Dados['Ctps'] != 0:
    Dados['Contratacao'] = int(input('Ano de contratacao: '))
    Dados['Salario'] = float(input('Salario: R$'))
    Dados['Aposentadoria'] = Dados['Idade'] + ((Dados['Contratacao'] + 35) - datetime.now().year)
print('-=' * 30)
for K, V in Dados.items():
    print(F'    - {K} tem o valor {V}')