'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''

Aluno = dict()
Aluno['Nome'] = str(input('Nome: '))
Aluno['Media'] = float(input(F'Media de {Aluno["Nome"]}: '))
if Aluno['Media'] >= 7:
    Aluno['Situacao'] = 'Aprovado'
elif 5 <= Aluno['Media'] < 7:
    Aluno['Situacao'] = 'Rescuperacao'
else:
    Aluno['Situacao'] = 'Reprovado'
print('-=' * 30)
for k, V in Aluno.items():
    print(F'{k} e iqual a {V}')