'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que leia um numero inteiro e mostre na tela se ele e PAR ou IMPAR.
'''

Numero  = int(input('Me diga um numero qualquer: '))
Resultado = Numero % 2
if Resultado == 0:
    print(F'O numero {Numero} e PAR.')
else:
    print(F'O numero {Numero} e IMPAR')