'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

Palavras = ('Aprender', 'Programar', 'Linquagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Programador', 'futuro')
for P in Palavras:
    print(F'\nNa palavra {P.upper()} temos')
    for Letra in P:
        if Letra.lower() in 'ae':
            print(Letra)