# crie um programa que leia o nome completo de uma pessoa e mostre :
# 1 O nome com as letras maisculas
# 2 O nome com todas as letras minusculas
# 3 qauntas letras tem ao total sem considerar os espaços
# 4 quantas tem o primeiro nome

nome = str(input('Digite seu nome completo:'))
x = nome.split()
y = len(x[0])
z = len(nome.replace(" ",""))

print(f'Maisculo:{nome.upper()}')

print(f'Minusculo:{nome.lower()}')

print(f'O seu nome ao todo tem {z} letras')

print(f'O Seu primeiro nome tem: {y} letras')



