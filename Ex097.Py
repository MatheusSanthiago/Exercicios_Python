'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
'''

def escreva(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'    {msg}')
    print('-' * tam)

escreva('Matheus Santhiago')
escreva('Curso de python no youtube')
escreva('Cev')