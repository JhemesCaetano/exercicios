# crie um programa que leie o peso e a altura de uma pessoa e calcule o seu IMC e mostre seu status de
# de acordo com a tabela abaixo
# abaixo de 18.5: abaixo do peso
# entre 18.5 e 25: peso ideal:
# 25 até 30: sobrepeso
# 30 té 40: obesidade
# acima de 40 : obsidade morbida:

peso = float(input('Digite seu peso em KG:'))
altura = float(input('Digite a sua altura em METROS:'))
imc = peso / (altura * altura)
if imc < 18.5:
    print(f'Seu IMC é:{imc:.2f}, E Você está abaixo do peso')
elif imc == 18 or imc < 25:
    print(f'Seu IMC é:{imc:.2f}, E você está no peso ideal')
elif imc == 25 or imc < 30:
    print(f'Seu IMC é:{imc:.2f}, E você está com sobrepeso')
elif imc == 30 or imc < 40:
    print(f'Seu IMC é:{imc:.2f}, E você está com obesidade')
elif imc >= 40:
    print(f'Seu IMC é:{imc:.2f}, E você está com obsidade morbida')
