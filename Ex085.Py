'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''

Num =[[], []]
Valor = 0
for C in range(1 ,8):
    Valor = int(input(F'Digite o {C}o. valor: '))
    if Valor % 2 == 0:
        Num[0].append(Valor)
    else:
        Num[1].append(Valor)
print('-=' * 30)
Num[0].sort()
Num[1].sort()
print(F'Os valores pares digitados foram: {Num[0]}')
print(F'Os valores impares digitados foram: {Num[1]}')