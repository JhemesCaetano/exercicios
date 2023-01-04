#Escreva um programa que leia a velocidade de um carro
#Se ele ultrapassar os 80km/h, mostre um mensagens que ele foi multado
#A multa vai custar R$7,00 por km acima do limite

velocidade = int(input('Qual é a velocidade que você está dirigindo seu carro?:'))
multa = (velocidade-80)*7
if velocidade > 80:
    print('Você foi multado por exceder o limite de velocidade')
    print(f'O valor a pagar da  multa é de:R${multa},00')

elif velocidade < 50:
        print("Você está devagar de mais , acelera um pouco ai ")

else:
    print("Parabéns você está dentro do limite de velocidade")
