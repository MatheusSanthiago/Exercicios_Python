'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''

Ficha = list()
while True:
    Nome = str(input('Nome: '))
    Nota1 = int(input('Nota 1: '))
    Nota2 = int(input('Nota 2: '))
    Media = (Nota1 + Nota2) / 2
    Ficha.append(Nome, [Nota1, Nota2], Media)
    Resp = str(input('Quer continuar? [S/N]'))
    if Resp in 'Nn':
        break
print('-=' * 30)
print(F'{"No.":<4}{"Nome":<10}{"Media":>8}')
print('-=' * 26)
for I, A in enumerate(Ficha):
    print(F'{I:<4}{A[0]:<10}{A[2]:>8.1f}')
while True:
    print('-' * 35)
    Opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if Opc == 999:
        print('FINALIZANDO...')
        break
    if Opc <= len(Ficha) - 1:
        print(F'Notas de {Ficha[Opc][0]} sao {Ficha[Opc][1]}')
print('<<< VOLTE SEMPRE >>>')