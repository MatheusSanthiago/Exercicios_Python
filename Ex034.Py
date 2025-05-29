'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Escreva um programa que pergunte o salario em funcionario e calcule o valor do seu aumento
Para salarios superiores a R$1.250,00, calcule um aumento de 10%
Para os salarios inferiores ou iquais, o aumento e de 15%.
'''

Salario = float(input('Qual e o salario do funcionario? R$'))
if Salario <= 1250:
    Novo = Salario + (Salario * 15 / 100)
else:
    Novo = Salario + (Salario * 10 / 100)
print(F'Quem ganhava R${Salario} passa a ganhar R${Novo} agora.')