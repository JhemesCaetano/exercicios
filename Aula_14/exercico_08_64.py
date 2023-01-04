# crie um programa que leia varios Números inteiros pelo teclado.O programa só vai parar , quando o usuario
# digitar o valor 999, que  é a condição de parada. no final mostrequantos numeros foram registrados e qual
# foi a soma de entre eles( desconsidere o frag)
n = 0
s = 0
c = 0
while n != 999:
    print('(digitando "999" o programa para)')
    n = int(input('Digite um valor:'))
    if n != 999:
        s += n
        c += 1
print(c, s)
