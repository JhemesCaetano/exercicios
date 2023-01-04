# crie um programa que leia o peso de 5 pessoas , e diga qual é o maior e qual é o menor peso lidos
maior_peso = 0
menor_peso = 0
for c in range(0, 5):
    peso = float(input(f'Digite o peso da {c + 1}ª:'))
    if c == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso < menor_peso:
            menor_peso = peso
        if peso > maior_peso:
            maior_peso = peso
print(f"o maior peso é :'{maior_peso}'")
print(f"o menor peso é :'{menor_peso}'")
 
