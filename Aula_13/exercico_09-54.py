# crie um programa que leia o ano de nascimento de 7 pessoas. e no final mostre quantas  pesssoas ainda não atingiram
# a maioridade e quantas já são maiores.
from datetime import date
maiores = 0
menores = 0
ano_atual = date.today().year
for people in range(0, 7):
    idade = int(input(f'Digite o ano de nascimento da {people + 1}ª:'))
    if ano_atual - idade < 21:
        menores += 1
    else:
        maiores += 1
print(f'''A quantidade de maiores de idade do grupo é:"{maiores}"
já a quantidades de menores de idade do grupo é:"{menores}"''')
print(f'o ano atual é:{ano_atual}')

