'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
'''

from math import radians, sin, cos, tan
Angulo = float(input('Digite o angulo que voce deseja: '))
Seno = sin(radians(Angulo))
print(F'O angulo de {Angulo} tem o seno de {Seno}')
cosseno = cos(radians(Angulo))
print(F'O angulo de {Angulo} tem o cosseno de {cosseno}')
Tangente = tan(radians(Angulo))
print(F'O angulo de {Angulo} tem a tangente de {Tangente}')