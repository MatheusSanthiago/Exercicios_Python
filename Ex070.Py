'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
'''

Total = TotMil = Menor = Cont = 0
Barato = ' '
while True:
    Produto = str(input('Nome do produto: '))
    Preco = float(input('Preco: R$'))
    Cont += 1
    Total += Preco
    if Preco > 1000:
        TotMil += 1
    if Cont == 1 or Preco < Menor:
        Menor = Preco
        Barato = Produto
    Resp = ' '
    while Resp not in "SN":
        Resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if Resp == 'N':
        break
print('Fim do Programa')
print(F'O total da compra foi R${Total:.2f}')
print(F'Temos {TotMil} produtos custando mais de R$1000.00')
print(F'O produto mais barato foi {Barato} que custa R${Menor:.2f}')