'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faca um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tintas necessaria para pinta-la, sabendo que cada litro
de tinta, pinta uma area de 2m.
'''
Larg = float(input('Largura da parede: '))
Alt = float(input('Altura da parede: '))
Area = Larg / Alt
print(F'Sua parede tem a dimensao de {Larg}x{Alt} e sua area e de {Area}m2')
Tinta = Area / 2
print(F'Para pintas essa parede, voce precisara de {Tinta}L de tinta')