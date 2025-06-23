'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado:  Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
Quantidade de notas
A maior nota
A menor nota
A média da turma
A situação (opcional).
'''

def Notas(*N, sit = False):
    R = dict()
    R['Total'] = len(N)
    R['Maior'] = max(N)
    R['Menor'] = min(N)
    R['Media'] = sum(N)/len(N)
    if sit:
        if R['Media'] >= 7:
            R['Situacao'] = 'Boa'
        elif R['Media'] >= 5:
            R['Situacao'] = 'Razoavel'
        else:
            R['Situacao'] = 'Ruim'
    return R

Resp = Notas(5.5, 2.5, 1.5, sit = True)
print(Resp)
help(Notas)