'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
'''

from time import sleep
C = ('\033[m',
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[0;30;44m',
     '\033[0;30;45m',
     '\033[7;30m'
     )
def Ajuda(Com):
    Titulo(F'Acessando o manual do comando \'{Com}\'', 4)
    print(C[6], end = '')
    help(Com)
    print(C[0], end = '')
    sleep(2)
def Titulo(Msg, Cor = 0):
    Tam = len(Msg) + 4
    print(C[Cor], end = '')
    print('-' * Tam)
    print(F'    {Msg}')
    print('-' * Tam)
    print(C[0], end = '')
    sleep(1)
while True:
    Titulo('Sistema de ajuda PyHelp', 2)
    Comando = str(input('Funcao ou biblioteca > '))
    if Comando.upper() == 'Fim':
        break
    else:
        Ajuda(Comando)
Titulo('Ate logo!', 1)