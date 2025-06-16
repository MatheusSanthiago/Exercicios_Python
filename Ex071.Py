'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

print('-' * 30)
print('Banco Cev')
print('=' * 30)
Valor = int(input('Que valor voce quer sacar? R$'))
Total = Valor
Ced = 50
TotCed = 0
while True:
    if Total >= Ced:
        Total -= Ced
        TotCed += 1
    else:
        if TotCed > 0:
            print(F'Total de {TotCed} cedulas de R${Ced}')
        if Ced == 50:
            Ced = 20
        elif Ced == 20:
            Ced = 10
        elif Ced == 10:
            Ced = 1
        TotCed = 0
        if Total == 0:
            break
print('=' * 30)
print('Volte sempre ao banco cev! Tenha um bom dia!')