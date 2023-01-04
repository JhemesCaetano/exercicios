# crie um programa que leia varios numeros inteiros pelo teclado. no final da execução , mostre a media entre
# os valores digitados e qual foi o maior e o menor valores lidos. o programa deve perguntar ao usuario se ele quer
# continuar ou não digitando valores
soma = 0
cont = 0
maior = 0
menor = 0
opcao = 's'
while opcao == 's' and opcao != 'n':
    v = int(input('digite um valor:'))
    soma += v
    cont += 1
    if menor == 0 and maior == 0:
        menor = v
        maior = v
    else:
        if v > maior:
            maior = v
        if v < menor:
            menor = v
    opcao = str(input('Deseja continuar escrevendo valores ?[S/N]:')).lower().strip()
    if opcao != 's':
        print('Acho que isso é um não ...')
media = soma / cont
print(f'''Você digitou "{cont}" valores, sendo o maior deles "{maior}" e o menor "{menor}".
A media dos valores digitados é "{media:.2f}"''')
