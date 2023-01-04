#escreva um programa que faça o computador
#pensar em um numero inteiro entre 0 e 5
#e peça para o usuario  tentar descobrir
#qual foi o numero escolhido pelo computador
#o programa devera escrever na tela se o usuario venceu ou perdeu
import random
print("Tente advinhar qual é numero escolhido pelo computador")
print("Ele está entre o numero 1 até o 5")
numero_u = int(input("Digite o numero:"))
numero_m = random.randrange(1, 6)

if numero_u == numero_m:
    print('PARABÉNS! Você acertou')
else:
    print(f'Desculpa você errou :(\nNumero correto era:{numero_m}')