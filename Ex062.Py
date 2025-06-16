'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
'''

print('Gerador de PA')
print('-=' * 10)
Primeiro = int(input('Primeiro termo: '))
Razao = int(input('Razao da PA: '))
Termo = Primeiro
Cont = 1
Total = 0
Mais = 10
while Mais != 0:
    Total = Total + Mais
    while Cont <= Total:
        print(F'{Termo}')
        Termo += Razao
        Cont += 1
    print('Pausa!')
    Mais = int(input('Quantos termo voce quer mostrar a mais? '))
print('Fim')