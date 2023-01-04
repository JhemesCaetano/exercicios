#crie um programa que faça o computador jogar jokenpô com você
import  random



print('=========================')
print('===Vamos jogar jokenpô===')
print('=========================')
jogador = str(input('Digite "pedra", "papel" ou "tesoura":')).lower()
cpu = random.choice(['Papel','Tesoura','Pedra'])
print(f'computador jogou {cpu}')
if 'tesoura' in jogador and 'Pedra' in cpu:
    print('Parabéns Você ganhou!!!')
elif 'pedra' in jogador and 'Tesoura' in cpu:
    print('Parabéns Você ganhou!!!')
elif 'papel' in jogador and 'Pedra' in cpu:
    print('Parabéns Você ganhou!!!')
elif "papel" in jogador and 'Tesoura' in cpu:
    print('Você perdeu ...')
elif 'pedra' in jogador and 'Papel' in cpu:
    print('Você perdeu ...')
elif 'tesoura' in jogador and 'Pedra' in cpu:
    print('Você perdeu ...')
elif 'pedra' in jogador and 'Pedra' in cpu:
    print('Deu empate...')
elif 'tesoura' in jogador and 'Tesoura' in cpu:
    print('Deu empate...')
elif 'papel' in jogador and 'Papel' in cpu:
    print('Deu empate...')
else:
    print("Sua jogada não é valida...")
