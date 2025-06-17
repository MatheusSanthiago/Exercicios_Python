'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

Temp = []
Princ = []
Mai = Men = 0
while True:
    Temp.append(str(input('Nome: ')))
    Temp.append(float(input('Peso: ')))
    if len(Princ) == 0:
        Mai = Men = Temp[1]
    else:
        if Temp[1] > Mai:
            Mai = Temp[1]
        if Temp[1] < Men:
            Men = Temp[1]
    Princ.append(Temp[:])
    Temp.clear()
    Resp = str(input('Quer continuar? [S/N]'))
    if Resp in 'Nn':
        break
print('-=' * 30)
print(F'Os dados foram {Princ}')
print(F'Ao todo, voce cadastrou {len(Princ)} pessoas. Peso de ', end='')
print(F'O maior peso foi de {Mai}Kg')
for P in Princ:
    if P[1] == Mai:
        print(F'p[0]', end = '')
print()
print(F'O menor peso foi de {Men}Kg')
for P in Princ:
    if P[1] == Men:
        print(F'[{P[0]}]', end = '')
print()