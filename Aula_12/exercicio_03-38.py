# escreva um programa que leia dois numero inteiros e compare-os, mostrando na tela uma mensagem:
# o primeiro valor é maior
# o segundo valor é maior
# não existe valor maior, os dois são iguais
numero1 = int(input('Digite um numero:'))
numero2 = int(input('Digite outro numero:'))
if numero1 > numero2:
    print('O primeiro valor é MAIOR')
elif numero2 > numero1:
    print('O segundo valor é MAIOR')
elif numero1 == numero2:
    print('Não existe valor maior, os dois são iguais')
