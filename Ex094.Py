'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média.
'''

from operator import itemgetter
Galera = list()
Pessoa = dict()
Soma = Media = 0
while True:
    Pessoa.clear()
    Pessoa['Nome'] = str(input('Nome: '))
    while True:
        Pessoa['Sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if Pessoa['Sexo'] in 'MF':
            break
        print('ERRO! por favor, digite apenas M ou F.')
    Pessoa['Idade'] = int(input('Idade: '))
    Galera.append(Pessoa.copy())
    while True:
        Resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if Resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if Resp == 'N':
        break
print('-=' * 30)
print(F'A) Ao todo temos {len(Galera)} pessoas cadastradas.')
Media = Soma / len(Galera)
print(F'B) A media de idade e de {Media:5.2f} anos')
print('C as mulheres cadastradas foram', end = '')
for P in Galera:
    if P['Sexo'] in "Ff":
        print(F'{P['Noem']} ', end = '')
print()
print('D) Lista das pessoas que estao acima da media: ')
for P in Galera:
    if P['Idade'] >= Media:
        print('     ')
        for K, V in P.items():
            print(F'{K} = {V}: ', end = '')
        print()
print('<< ENCERRADO >>')