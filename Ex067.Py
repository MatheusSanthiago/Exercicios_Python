'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado:  Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''

while True:
    N = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if N < 0:
        break
    for C in range(1, 11):
        print(F'{N} x {C} = {N * C}')
    print('-' * 30)
print('Programa tabuada encerrada. Volte sempre!')