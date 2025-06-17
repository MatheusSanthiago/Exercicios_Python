'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

Valores = []
while True:
    Valores.append(int(input('Digite um valor: ')))
    Resp = str(input('Quer continuar? [S/N]'))
    if Resp in 'Nn':
        break
print('-=' * 30)
print(F'Voce digitou {len(Valores)} Elementos.')
Valores.sort(reverse=True)
print(F'O valores em ordem decrecente sao {Valores}')
if 5 in Valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 nao foi encontrado na lista!')