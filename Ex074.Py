'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

from random import randint
Numeros = (randint(1, 10), randint(1, 10), randint(1 , 10), randint(1, 10), randint(1 , 10))
print('Os valores sorteados foram: ')
for N in Numeros:
    print(F'{N}')
print(F'\nO maior valor sorteado foi {max(Numeros)}')
print(F'O menor valor sorteado foi {min(Numeros)}')