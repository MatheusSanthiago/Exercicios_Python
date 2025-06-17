'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

Lista = ('Lapis', 1.75,'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 40)
print('Listagem de precos')
print('-' * 40)
for Pos in range(0, len(Lista)):
    if Pos % 2 == 0:
        print(F'{Lista[Pos]}')
    else:
        print(F'R${Lista[Pos]:>7.2f}')
print('-' * 40)