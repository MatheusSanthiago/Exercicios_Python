'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''


def area(largura, comprimeto):
    A = largura * comprimeto
    print(F'A area de um terreno {largura}x{comprimeto} e de {A}m')

print(' Controle de terrenos')
print('-' * 20)
L = float(input('Largura (m): '))
C = float(input('Comprimento (M): '))
area(L, C)