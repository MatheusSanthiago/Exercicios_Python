'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
'''

from math import hypot
Co = float(input('Comprimento do cateto oposto: '))
Ca = float(input('Comprimento do cateto adjacente: '))
Hi = hypot(Co, Ca)
print(F'A hipotenusa vai medir {Hi}')