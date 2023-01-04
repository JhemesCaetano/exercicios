# crie um programa que leia dois valores e mostre um menu na tela:
# [1] = somar
# [2] = multiplicar
# [3] = maior
# [4] = novos Números
# [5] = sair do programa
print('-==-=-=-=-=-=-=Bem vindo=-=-=-=-=-=-=-=')
valor_1 = int(input('Digite o primeiro valor:'))
valor_2 = int(input('Digite o segundo valor:'))

opcao = 0
while opcao != 5:
    print('-==-=-=-=-=-=-=Menu=-=-=-=-=-=-=-=')
    print('''Oque vamos fazer com os valores ?:
-=-=-=-=-=-=-=-=-=-=-=-=
[1] = Somar
[2] = Multiplicar
[3] = Maior entre os valores
[4] = Digitar novos Valores
[5] = Sair do programa''')
    opcao = int(input('-=-=-=-=-=-=-=-=-=-=-=-=:'))
    if opcao == 1:
        somar = valor_1 + valor_2
        print(f'A soma dos valores {valor_1} + {valor_2}, é ="{somar}"')
    if opcao == 2:
        multiplicar = valor_1 * valor_2
        print(f'A multiplicação dos valores {valor_1} X {valor_2}, é ="{multiplicar}"')
    if opcao == 3:
        if valor_1 > valor_2:
            print(f'O primeiro valor "{valor_1}" é o maior entre eles ')
        else:
            print(f'O segundo valor "{valor_2}" é o maior entre eles ')
    if opcao == 4:
        valor_1 = int(input('Digite o novo primeiro valor:'))
        valor_2 = int(input('Digite o novo segundo valor:'))

print("até mais...")



