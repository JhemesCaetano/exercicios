#crie um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
#para salarios acima de R$1250.00 calcule um aumento de 10%
#para salarios abaixo de R$1250.00 calcule um aumento de 15%
import math

salario = float(input('Qual é o seu salrio atual?\nR$:'))
aumento1 = (10 * salario) / 100 + salario
aumento2 = (15 * salario) / 100 + salario
if salario >= 1250.0:
    print(f"Você obteve um aumento de 10% e o seu salario vai ser R${aumento1:.2f}")
else:
    print(f'Você obteve um aumento de 15% e o seu salario vai ser R${aumento2:.2f}')


