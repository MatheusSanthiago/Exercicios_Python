'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a media atingida:
- Media abaixo de 5.0: REPROVADO
- Media entre 5.0 e 6.9: RECUPERACAO
- Media 7.0 ou superior: Aprovado.
'''

Nota1 = float(input('Primeira nota: '))
Nota2 = float(input('Segunda nota: '))
media = (Nota1 + Nota2) / 2
print(F'Tirando {Nota1:.1f} e {Nota2:.1f}, a media do aluno e {media:.1f}')
if 7 > media >= 5:
    print('O alunoenta em recupecao.')
elif media < 5:
    print('O aluno esta reprovado.')
elif media >= 7:
    print('O aluno esta aprovado.')