#crie um programa que leia o nome completo de uma pessoa e mostre o primeiro e o ultimo nome separadamente:
#ex : Digite o seu nome: Ana Maria de Souza
#primeor nome : Ana
#ultimo nome : Souza

nome = input('Digite seu nome:')
x = nome.split()
print(f'Seu primero nome é:{x[0]}')
print(f'Seu ultimo nome é:{x[-1]}')




