'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Faca um programa que leia uma frase pelo teclado e mostre:
> Quantas vazes aparece a letra "A"
> Em que posicao ela aparece a primeira vez
> Em que posicao ela aparece a iltima vez.
'''

Frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {} vezes na frase.'.format(Frase.count("A")))
print('A primeira letra "A" aparece na posicao {}'.format(Frase.find("A") + 1))
print('A ultima letra "A" apareceu na posicao {}'.format(Frase.rfind("A") + 1))