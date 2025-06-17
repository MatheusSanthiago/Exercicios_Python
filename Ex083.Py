'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

Expr = str(input('Digite a espressao: '))
Pilha = []
for Simb in Expr:
    if Simb == '(':
        Pilha.append('(')
    elif Simb == '(':
        if len(Pilha) > 0:
            Pilha.pop()
        else:
            Pilha.append('(')
            break
if len(Pilha) == 0:
    print('Sua expressao enta valida!')
else:
    print('Sua expressao esta errada!')