'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

Cont = ('Zero', 'Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Catorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')

while True:
    Num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= Num <= 20:
        break
    print('Tente novamente.')
print(F'Voce digitou o numero {Cont[Num]}')