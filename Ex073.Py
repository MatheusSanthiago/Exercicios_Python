'''
Nome:Matheus Santhiago Fortonato de Souza
Data:23/05/2025
Enunciado: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.
'''

Times = ('Corinthians','Palmeiras','Santos','Gremio','Cruzeiro','Flamengo','Vasco','Chapecoense','Atletico','Botafogo','Atletico-PR','Bahia','Sao Paulo','Fluminense','Sport Recife','Ec Vitoria','Coritiba','Avai','Ponte Preta','Atletico-GO')

print('-=' * 15)
print(F'Lista de times Brasoleirao: {Times}')
print('-=' * 15)
print(F'Os 5 primeiros sao: {Times[0:5]}')
print('-=' * 15)
print(F'Os 4 ultimos sao: {Times[-4]}')
print('-=' * 15)
print(F'Times em ordem alfabetica: {sorted(Times)}')
print('-=' * 15)
print(F'O chapecoense esta na: {Times.index('Chapecoense')}')
print('-=' * 15)