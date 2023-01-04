# crie um programa que leia um numero inteiro e diga se ele é um numero primo
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[34m', end= '')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end=',')
print(f'O número "{num}" foi divisível por "{tot}" vezes')
if tot == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele não é primo')
