'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
'''

Medida = float(input('uma distancia em metros: '))
Cm = Medida * 100
mm = Medida * 1000
print(F'A medida de {Medida}M corresponde a {Cm}Cm e {mm}mm')