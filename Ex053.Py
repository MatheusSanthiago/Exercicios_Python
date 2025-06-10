'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: crie um programa que leia uma frase qualquer e diga se ela e um palindromo, desconsiderando os espacos.
'''

Frase = str(input('Digite uma frase: ')).strip().upper()
Palavras = Frase.split()
Junto = ''.join(Palavras)
Inverso = Junto[::-1]
print(F'O inverso de {Junto} e {Inverso}')
if Inverso == Junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada nao e um palindromo!')