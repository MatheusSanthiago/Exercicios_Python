'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente..
'''

Numeros = list()
while True:
    N = int(input('Digite um valor: '))
    if N not in Numeros:
        Numeros.append(N)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor Duplicado! Nao vou adicionar...')
    R = str(input('Quer continuar? [S/N] '))
    if R in "Nn":
        break
print('-=' * 30)
Numeros.sort()
print(F'Voce digitou os valores {Numeros}')