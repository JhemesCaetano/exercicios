#crie um programa que leia o nome de uma pessoa e diga se ela contem o nome "silva"

nome = str(input('Digite seu nome:'))

if 'silva' in nome.lower():
    print('Seu nome tem "silva"')

else:
    print('Seu nome não tem "silva"')
    