#refaça o desafio 51 , lendo o primeiro termo e a razão de uma PA, mostrando os 10  primeiros termos da
#progresão usando a estrutura while
t = int(input("Digite o primeiro termo da PA:"))
r = int(input('Digite a Razão da PA:'))
final = 1
comeco = t - r
while final != 11:
    final += 1
    comeco += r
    print(comeco)
