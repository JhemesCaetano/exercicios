#crie um programa que leia 3 numeros e diga qual é o maior e qual é o menor
numero1 = int(input("Digite o primeiro valor:"))
numero2 = int(input('Digite o segundo valor:'))
numero3 = int(input('Digite o terceiro valor:'))
menor = numero1
maior = numero1
# verificando o menor
if  numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero2:
    menor = numero3
# verificando o maior
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero1 and numero3 > numero2:
    maior = numero3
print(f'O numero maior é:"{maior}"')
print(f'O numero menor é:"{menor}"')
