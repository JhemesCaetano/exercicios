# crie um programa , que leia um numero inteiro qualquer e peça para o usuario escolher qual será a base de converção
# 1 para binario
# 2 para octal
# 3 para hexadecimal
while True:
    numero = int(input('Digite o numero a ser convertido:'))
    print('| MENU |')
    print('Escolha a base de converção:')
    opcao=int(input('1-Binario\n2-Octal\n3-Hexdecimal\n4-Sair\nDigite a opção desejada:'))
    if opcao == 1:
        print(f' O numero:"{numero}" convertido para Binario ficará assim:"{bin(numero)[2:]}"')
    elif opcao == 2:
        print(f' O numero:"{numero}" convertido para Octal ficará assim:"{oct(numero)[2:]}"')
    elif opcao == 3:
        print(f' O numero:"{numero}" convertido para Hexadecimal ficará assim:"{hex(numero)[2:]}"')
    elif opcao == 4:
        print('Até mais ...')
        break
    else:
        print('Opção invalida\nO programa será finalizado')
        break
