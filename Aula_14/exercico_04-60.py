# faça um programa que leia um numero qualquer e mostre o seu fatorial
# com (for)
#numero = int(input('Digite um numero:'))
#fatorial = numero * (numero - 1)
#for n in range(numero - 2, 0, -1):
    #fatorial = fatorial * n
#print(f'o fatorial do numero, "{numero}" é = "{fatorial}"')
numero = int(input('Digite um numero:'))
multiplo = numero
fatorial = numero
while multiplo != 1:
    multiplo = multiplo - 1
    fatorial = fatorial * multiplo
print(f'O fatorial do numero,"{numero}" é = "{fatorial}"')
