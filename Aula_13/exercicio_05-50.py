# faça um programa que leia  seis números inteiros e mostre  a soma apenas daqueles que forem pare.
# se o valor for impares desconsidere
soma = 0
cont = 0
for l in range(1, 7):
    n = int(input('Digite um numero:'))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f' Você informou,"{cont}" numeros pares e a soma entres eles é:"{soma}"')