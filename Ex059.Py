'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

N1 = int(input('Primeiro valor: '))
N2 = int(input('Segundo valor: '))
Opcao = 0
while Opcao != 5:
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos numeros
    [ 5 ] Sair do programa
    ''')
    if Opcao == 1:
        Soma = N1 + N2
        print(F'A soma entre {N1} e {N2} e {Soma}')
    elif Opcao == 2:
        Produto = N1 * N2
        print(F'A Resultado de {N1} x {N2} e {Produto}')
    elif Opcao == 3:
        if N1 > N2:
            Maior = N1
        else:
            Maior = N2
        print(F'Entre {N1} e {N2} o maior valor e {Maior}')
    elif Opcao == 4:
        print('Informe os numero Novamente: ')
        N1 = int(input('Primeiro valor: '))
        N2 = int(input('Segundo valor: '))