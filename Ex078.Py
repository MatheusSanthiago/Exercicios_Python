'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''

ListaNum = []
Mai = 0
Men = 0
for C in range(0, 5):
    ListaNum.append(int(input(F'Digite um valor para a posicao {C}')))
    if C == 0:
        Mai = Men = ListaNum[C]
    else:
        if ListaNum[C] > Mai:
            Mai = ListaNum[C]
        if ListaNum[C] < Men:
            Men = ListaNum[C]
print('=-' * 30)
print(F'Voce digitou os valores {ListaNum}')
print(F'O maior valor digitado foi {Mai} nas posicoes')
for I, V in enumerate(ListaNum):
    if V == Mai:
        print(F'{I}...')
print()
print(F'O menor valor digitado foi {Men} nas posicoes')
for I, V in enumerate(ListaNum):
    if V == Men:
        print(F'{I}...')
print()