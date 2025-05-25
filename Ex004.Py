'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faca um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informacoes possiveis sobre ela.
'''

A = input('Digite algo: ')
print('O tipo primitivo desse valor e: ', type(A))
print('So tem espacos? ', A.isspace())
print('E um numero? ', A.isnumeric())
print('E alfabetico? ', A.isalpha())
print('A alfanumerico? ', A.isalnum())
print('Esta em maiusculo ?', A.isupper())
print('Esta em minusculo ?', A.islower())
print('Esta capitalizada ?', A.istitle())