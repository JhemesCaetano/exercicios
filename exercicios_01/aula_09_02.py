#faça um programa que leia um numero de 0 até 9999 e mostre na tela cada um dos digitos separados
# ex : Digite um numero : 1834
#unidade:4
#Dezena:3
#centena:8
#milhar:1
numero = int(input('Digite um numero de 0 até 9999:'))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f'O numero: {numero} contem:')
print(f"Unidade: {u}")
print(f'Dezena: {d}')
print(f'Centana: {c}')
print(f'Milhar: {m}')
