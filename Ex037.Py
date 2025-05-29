'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Escreva um programa que leia um numero inteiro qualquer e peca para o usuario escolher qual sera a base de conversao.
'''

Num = int(input('Digite um numero inteiro: '))
print(''' Escolha uma das bases para conversao:
[ 1 ] Converter para binario
[ 2 ] Converter para octal
[ 3 ] Converter para hexadecimal
''')
Opcao = int(input('Sua opcao: '))
if Opcao == 1:
    print(F'{Num} Convertido para binario e iqual a {bin(Num)}')
elif Opcao == 2:
    print(F'{Num} Convertido para octal e iqual a {oct(Num)}')
elif Opcao == 3:
    print(F'{Num} Convertido para hexadecimal e iqual a {hex(Num)}')
else:
    print('Opcao invalida tente novamente.')