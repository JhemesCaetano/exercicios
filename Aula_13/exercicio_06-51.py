#desenvolva um programa um programa que leia o primeiro termo de uma progreção aritimetica.
# no final, mostre  os 10 primeiros termos dessa  progressão
t = int(input('Digite o primeiro termo da progreção:'))
r = int(input('Digite a razão da progreção:'))
s = r * 10 + t
for r in range(t, s, r):
    print(r)
