'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

Resp = 'S'
Soma = Quant = Media = Maior = Menor = 0
while Resp in 'Ss':
    Num = int(input('Digite um numero: '))
    Soma += Num
    Quant += 1
    if Quant == 1:
        Maior = Menor = Num
    else:
        if Num > Maior:
            Maior = Num
        if Num < Menor:
            Menor = Num
    Resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
Media = Soma / Quant
print(F'Voce digitou {Quant} Numeros e a media foiu {Media}')
print(F'o maior valor foi {Maior} e o menor foi {Menor}')