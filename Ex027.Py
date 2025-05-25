'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faca um programa que leia o nome compelto de uma pessoa mostrando em seguida o primeiro e o ultimo nome separadamente.
'''

N = str(input('Digite seu nome compelto: ')).strip()
Nome = N.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome e {}'.format(Nome[0]))
print('Seu ultimo nome e {}'.format(Nome[len(Nome) - 1]))