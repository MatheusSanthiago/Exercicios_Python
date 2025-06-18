'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''

Time = list()
Jogador = dict()
Partidas = list()
from operator import itemgetter
while True:
    Jogador.clear()
    Jogador['Nome'] = str(input('Nome do jogador: '))
    Tot = int(input(F'Quantas partidas {Jogador['Nome']} jogou? '))
    Partidas.clear()
    for C in range(0, Tot):
        Partidas.append(int(input(F'    Quantos gols na partida {C+1}?')))
    Jogador['Gols'] = Partidas[:]
    Jogador['Total'] = sum(Partidas)
    Time.append(Jogador.copy())
    while True:
        Resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if Resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if Resp == 'N':
        break
print('-' * 30)
print('Cod ', end = '')
for I in Jogador.keys():
    print(F'{I:<15}', end = '')
print()
print('-' * 40)
for K, V in enumerate(Time):
    print(F'{K:>3}', end = '')
    for D in V.values():
        print(F'{str(D):<15}', end = '')
    print()
print('-' * 40) 
while True:
    Busca = int(input('Mostrar dados de qual jogador (999 para parar)'))
    if Busca == 999:
        break
    if Busca >= len(Time):
        print(F'Erro! Nao existe jogador com codigo {Busca}!')
    else:
        print(F'    -- LEVANTAMENTO DO JOGADOR {Time[Busca]['Nome']}:')
        for I, G in enumerate(Time[Busca]['Gols']):
            print(F'    No jogo{I+1} fez {G} gols')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')