'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''

SomaIdade = 0
MediaIdade = 0
MaiorIdadeHomen = 0
NomeVelho = ''
TotMulher20 = 0
for P in range(1, 5):
    print('-------------- {}Pessoa --------------')
    Nome = str(input('Nome: ')).strip()
    Idade = int(input('Idade: '))
    Sexo =- str(input('Sexo [M/F]: ')).strip()
    SomaIdade += Idade
    if P == 1 and Sexo in 'Mm':
        MaiorIdadeHomen = Idade
        NomeVelho = Nome
    if Sexo in 'Mm' and Idade > MaiorIdadeHomen:
        MaiorIdadeHomen = Idade
        NomeVelho = Nome
    if Sexo in 'Ff' and Idade < 20:
        TotMulher20 += 1
MediaIdade = SomaIdade / 4
print(F'A media de idade do grupo e de {MediaIdade} anos')
print(F'O hoemn mais velho tem {MaiorIdadeHomen} anos e se chama {NomeVelho}')
print(F'Ao todo sao {TotMulher20} mulheres com menos de 20 anos')