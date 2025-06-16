'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''

Num = Cont = Soma = 0
Num = int(input('Digite um numero [999 para parar]: '))
while Num != 999:
    Soma += Num
    Cont += 1
    Num = int(input('Digite um numero [999 para parar]: '))
print(F'Voce digitou {Cont} numeros e a soma entre eles foi {Soma}')