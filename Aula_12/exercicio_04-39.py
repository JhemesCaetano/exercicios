# crie um programa que leia o ano de nascimento e informe de acordo com a sua idade:
# se ele ainda vai se alistar ao serviço militar
# se já é a hora de se alistar
# se já passou do tempo de se alistar
# seu programa devera mostrar também o tempo que passou ou falta para o prazo
ano_nascimento = int(input('Digite o ano em que nasceu:'))
ano_atual = 2022
idade = ano_atual - ano_nascimento
tempo_excedente = idade - 18
tempo_de_sobra = 18 - idade
if idade < 18:
    print(f'Voce ainda vai se alistar, falta exatamente:"{tempo_de_sobra}" Anos para o alistamento.')
elif idade == 18:
    print('Está na hora de se alistar , boa sorte.')
elif idade > 18:
    print(f'Já passou da hora de se alistar, você está a exatamente:"{tempo_excedente}" Anos atrasado para o alistamento')
