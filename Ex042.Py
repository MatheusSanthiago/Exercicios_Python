'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Refaca o enunciado/EX035.Py dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado.
'''
R1 = float(input('Primeiro segmento: '))
R2 = float(input('Segundo segmento: '))
R3 = float(input('Terceiro segmento: '))
if R1 < R2 + R3 and R2 < R1 + R3 and R3 < R1 + R2:
    print('Os segmentos acima podem formar um triangulo')
    if R1 == R2 == R3:
        print('Equilatero')
    elif R1 != R2 != R3 != R1:
        print('Escaleno!')
    else:
        print('Isoceles')
else:
    print('Os segmentos acima nao podem formar triangulo')