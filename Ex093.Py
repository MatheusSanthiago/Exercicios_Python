'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

Jogador = dict()
Partidas = list()
Jogador['Nome'] = str(input('Nome do jogador: '))
Tot = int(input(F'Quantas partidas {Jogador['Nome']} jogou? '))
for C in range(0,  Tot):
    Partidas.append(int(input(F'    Quantos gols na partida {C}? ')))
Jogador['Gols'] = Partidas[:]
Jogador['Total'] = sum(Partidas)
print('-=' * 30)
print(Jogador)
print('-=' * 30)
for K, V in Jogador.items():
    print(F'O campo {K} tem o valor {V}')
print('-=' - 30)
print(F'O jogador {Jogador['Nome']} jogou {len(Jogador['Gols'])} partidas.')
for I, V in enumerate(Jogador['Gols']):
    print(F'    => Na partida {I}, fez {V} gols.')
print(F'Foi um total de {Jogador['Total']} Gols')