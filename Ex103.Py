'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''

def Ficha(Jog = '<Desconhecido>', Gol = 0) :
    print(F'O jogador {Jog} fez {Gol} gol(s) no campeonato.')


N = str(input('Nome do jogador: '))
G = str(input('Numero de Gols: '))
if G.isnumeric():
    G = int(G)
else:
    G = 0
if N.strip() == '':
    Ficha(Gol = G)
else:
    Ficha(N, G)