'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

Sexo = str(input('Informe seu sexo [M/F] ')).strip().upper()
while Sexo not in 'MmFf':
    Sexo = str(input('Dados invalidos. Por favorn informe seu sexo:')).strip().upper()
print(F'Sexo {Sexo} registrado com sucesso')