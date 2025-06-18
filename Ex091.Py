'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''

from random import randint
from time import sleep
from operator import itemgetter
Jogo = {'Jogador1': randint(1, 6), 'Jogador2': randint(1, 6), 'Jogador3': randint(1, 6), 'Jogador4': randint(1, 6),}
Ranking = list()
print('Valores sorteados: ')
for K, V in Jogo.items():
    print(F'{K}, tirou {V} no dado.')
    sleep(1)
Ranking = sorted(Jogo.items(), key = itemgetter(1), reverse=True)
print('-=' * 30)
print(' ==  RANKING DOS JOGADORES  ==')
for I, V in enumerate(Ranking):
    print(F'    {I+1} Lugar: {V[0]} com {V[1]}')