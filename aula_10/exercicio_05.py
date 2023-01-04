#Crie um programa que leia um ano e diga se ele é bicesto ou não
ano = int(input('Digite um ano:'))
if (ano % 4) == 0:
    print('Esse ano é "Bisesto"')
else:
    print('Esse ano não é "Bisesto"')
