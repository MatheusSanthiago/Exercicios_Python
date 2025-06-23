'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ').
'''

def leiaInt(msg):
    Ok = False
    Valor = 0
    while True:
        N = str(input(msg))
        if N.isnumeric():
            Valor = int(N)
            Ok = True
        else:
            print('\033[0;31mERRO! Digite um numero inteiro valido.\033[m')
        if Ok:
            break
    return Valor

N = leiaInt('Digite um numero: ')
print(F'Voce acabou de digitar o numero {N}')