# a confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
# sua categoria de acordo com a sua idade:
# até 9 anos: mirim
# até 14 anos: infantial
# até 19 anos: junior
# até 20 anos: sênior
# Acima: master

ano = int(input('Digite seu ano de nascimento:'))
idade = 2022 - ano
if  idade <= 9:
    print('"Atleta Mirim"')
elif idade >= 10 and idade <= 14:
    print('"Atleta infantil"')
elif idade >= 15 and idade <= 19:
    print('"Atleta Junior"')
elif idade == 20:
    print('"Atleta Sênior"')
elif idade > 20:
    print('"Atleta Master"')
