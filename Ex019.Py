'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Um professor quer sortear um dos seus quatro alunos para apagar a quadro. faca um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''

from random import choice
N1 = str(input('Primeiro aluno: '))
N2 = str(input('Segundo aluno: '))
N3 = str(input('Terceiro aluno: '))
N4 = str(input('Quarto aluno: '))
Lista = [N1, N2, N3, N4]
Escolhido = choice(Lista)
print(F'O aluno escolhido foi {Escolhido}')