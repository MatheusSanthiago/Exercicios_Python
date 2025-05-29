'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa pergunte o valor da casa, o salario do comprador e em quantos anos ele vai pagar. A prestacao mensal, nao pode exceder 30% do salario ou entao o emprestimo sera negado.
'''

Casa = float(input('Valor da casa: R$'))
Salario = float(input('Salario do comprador: R$'))
Anos = int(input('Quantos anos de financiamento? '))
Prestacao = Casa / (Anos * 12)
Minimo = Salario * 30 / 100
print(F'Para pegar uma casa de R${Casa} em {Anos} anos')
print(F'A Prestacao sera de R${Prestacao}')
if Prestacao <= Minimo:
    print('Emprestimo pode ser concedido!')
else:
    print('Emprestimo negado!')