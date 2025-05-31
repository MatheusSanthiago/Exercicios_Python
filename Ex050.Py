'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que foram pares. Se o valor digitado for impar, desconsidere-o.
'''

Soma = 0
Cont = 0
for c in range(1, 7):
    Num = int(input(F'Digite o {c} valor:'))
    if Num % 2 == 0:
        Soma += Num
        Cont += 1
print(F'Voce informou {Cont} numeros pares e a soma foi {Soma}')