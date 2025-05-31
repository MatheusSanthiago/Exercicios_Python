'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
Abaixo de 18.5: Abaixo do peso
Entre 18.5 e 25: Peso ideal
25 ate 30: sobrepeso
30 ate 40: Obesidade
Acima de 40: Obsidade morbida.
'''

Peso = float(input('Qual e seu peso (Kg)'))
Altura = float(input('Qual e sua altura? (M)'))
Imc = Peso / (Altura ** 2)
print(F'O imc dessa pessoa e de {Imc:.1f}')
if Imc <18.5:
    print('Voce esta abixo do peso normal')
elif 18.5 <= Imc < 25:
    print('Parabnes, Voce esta na faixa de peso normal')
elif 25 <= Imc < 30:
    print('Voce esta em sobrepeso')
elif 30 <= Imc < 40:
    print('Voce esta em obesidade!')
elif Imc >= 40:
    print('Voce esta em obesidade morbida, cuidado!')