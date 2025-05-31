'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preco normal e condicao de pagamento:
- A vista dinheiro/cheque: 10% de desconto
- A vista no cartao: 5% de desconto
- Em ate 2x no cartao: preco normal
- 3x ou mais no cartao: 20% de juros.
'''

Preco = float(input('Preco das compras: R$'))
print('''Formas de pagamento
[ 1 ] A vista Dinheiro/Cheque
[ 2 ] A vista cartao
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao
''')
Opcao = int(input('Qual e a opcao?'))
if Opcao == 1:
    Total = Preco - (Preco * 10 / 100)
elif Opcao == 2:
    Total = Preco - (Preco * 5 / 100)
elif Opcao == 3:
    Total = Preco
    Parcela = Total / 2
    print(F'Sua compra sera parcelada em 2x de R${Parcela:.2f}')
print(F'Sua compra de R${Preco:.2f} vai custar R${Total:.2f} no final')