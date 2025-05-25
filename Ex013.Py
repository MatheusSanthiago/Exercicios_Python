'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faca um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.
'''

Salario = float(input('Qual e o salario do funcionario? R$ '))
Novo = Salario + (Salario *15 / 100)
print(F'Um funcionario que ganhava R${Salario}, com 15% de aumento, passa a receber R${Novo}')