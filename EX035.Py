'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo.
'''

print('-=' * 20)
print('Analisandor de triangulos')
print('-=' * 20)
R1 = float(input('Primeiro segmento: '))
R2 = float(input('Segundo segmento: '))
R3 = float(input('Terceiro segmento: '))
if R1 < R2 + R3 and R2 < R1 + R3 and R3 < R1 + R2:
    print('Os segmentos acima podem formar triangulo')
else:
    print('Os segmentos acima nao podem formar um triangulo')