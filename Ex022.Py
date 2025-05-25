'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que leia o nome completo de uma pessoa e mostre:
> O nome com todos as letras maiusculas e minusculas
> Quantas letras ao todo (sem considerar espacos)
> Quantas letras tem o primeiro nome.
'''

Nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
print('Seu nome em maiusculo e {}'.format(Nome.upper()))
print('Seu nome em minusculo e {}'.format(Nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(Nome) - Nome.count(' ')))
Separa = Nome.split()
print('Seu primeiro nome e {} e ele tem {} letras'.format(Separa(0), len(Separa[0])))