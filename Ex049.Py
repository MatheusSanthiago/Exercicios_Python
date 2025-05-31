'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Refaca o desafio 009, mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando um laco for.
'''

Num = int(input('Digite um numero para ver sua tabuada: '))
for c in range(1, 11):
    print(F'{Num} x {c:2} = {Num * c}')