# faça um programa QUE CALCULE A SOMA DE TODOS OS NUMEROS IMPARES QUE SÃO MULTIPLOS DE 3 que se encontram no
# intervalo de 1 até 500
soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        cont += 1
        soma += 1
print(f'a soma de todos os valores solicitados é {soma}, cont')
