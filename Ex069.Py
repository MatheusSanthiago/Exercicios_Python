'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado:  Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
'''

Tot18 = TotH = TotM20 = 0
while True:
    Idade = int(input('Idade: '))
    Sexo = ' '
    while Sexo not in 'MF':
        Sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if Idade >= 18:
        Tot18 += 1
    if Sexo == 'M':
        TotH += 1
    if Sexo == 'F' and Idade < 20:
        TotM20 += 1
    Resp = ' '
    while Resp not in "SN":
        Resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if Resp == 'N':
        break
print(F'Total de pessoas com masi de 18 anos: {Tot18}')
print(F'Ao todo temos {TotH} Homens cadastrados')
print(F'E temos {TotM20} mulheres com menos de 20 anos')