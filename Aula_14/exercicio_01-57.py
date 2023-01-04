# faça um programa que leia  o sexo , mas só aceite os valores 'm' ou 'f' Caso esteja errado
# peça a digitação novamente até ter um valor correto
sexo = ''.upper().strip()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
    if sexo == 'M' or sexo == 'F':
        print('obrigado por dizer seu sexo ^.^')
    else:
        print('Por favor digite um sexo valido.')
print(f'Você digitou que é do sexo "{sexo}", seu dado foi salvo , obrigado.')
