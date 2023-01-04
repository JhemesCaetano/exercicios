#recrie o desafio numero 28 onde o computador vai pensar em um numero de 0-10. só que agora o jogador vai jogar até
# até acertar , mostrando no final quantas tentativas ele precisou para vencer.
import random
import time
print("Tente advinhar qual é numero escolhido pelo computador")
print("Ele está entre o numero 1 até o 10")
number_cpu = random.randrange(1, 11)
number_player = 0
tentavias = 1
print(number_cpu)
while number_cpu != number_player:
    number_player = int(input("Digite sua jogada:"))
    if number_cpu == number_player:
        time.sleep(0.2)
        print('PARABÉNS , Você acertou!!!')
    else:
        if number_player < number_cpu:
            time.sleep(0.2)
            print("mais... Tenta mais uma vez...")
            tentavias += 1
        elif number_player > number_cpu:
            time.sleep(0.2)
            print('menos... Tente mais uma vez')
            tentavias += 1
print(f'foram necesario um total de,"{tentavias}" tentavivas para vc ganhar ^.^')
