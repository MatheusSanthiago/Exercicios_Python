'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''

Num = list()
Pares = list()
Impares = list()
while True:
    Num.append(int(input('Digite um numero: ')))
    Resp = str(input('Quer continuar? [S/N]'))
    if Resp in 'Nn':
        break
for I, V in enumerate(Num):
    if V % 2 == 0:
        Pares.append(V)
    elif V % 2 == 1:
        Impares.append(V)
print(F'A lista completa e {Num}')
print(F'A lista de pares e {Pares}')
print(F'A lista de impares e {Impares}')