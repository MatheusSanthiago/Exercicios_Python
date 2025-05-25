'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: O mesmo professor do desafio anterior quer sortear a ordem de apresentacao de trabalho dos alunos faca um programa que leia o nome dos quatro alunos e mostre a ordem
sorteada.
'''

from random import shuffle
N1 = str(input('Primeiro aluno: '))
N2 = str(input('Segundo aluno: '))
N3 = str(input('Terceiro aluno: '))
N4 = str(input('Quarto aluno: '))
Lista = [N1, N2, N3, N4]
shuffle(Lista)
print('A ordem de apresentacao sera: ')
print(Lista)