'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''

lista = []
for c in range(0, 5):
    N = int(input('Digite um valor: '))
    if c == 0 or N > lista[-1]:
        lista.append(N)
        print('Adicionado ao final da lista...')
    else:
        Pos = 0
        while Pos < len(lista):
            if N <= lista[Pos]:
                lista.insert(Pos, N)
                print(F'Adicionado na posicao {Pos} da lista...')
                break
            Pos += 1
print('-=' * 30)
print(F'Os valores digitados em ordem fora {lista}')