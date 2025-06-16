'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''

print('Gerador de PA')
print('-=' * 10)
Primeiro = int(input('Primeiro termo: '))
Razao = int(input('Razao da PA: '))
Termo = Primeiro
Cont = 1
while Cont <= 10:
    print(F'{Termo}')
    Termo += Razao
    Cont += 1
print('Fim')