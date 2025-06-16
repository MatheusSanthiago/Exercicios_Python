'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
'''

Soma = Cont = 0
while True:
    Num = int(input('Digite um valor (999 para parar): '))
    if Num == 999:
        break
    Cont += 1
    Soma += Num
print(F'A soma dos {Cont} valores foi {Soma}!')