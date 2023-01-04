# escreva um programa para aprovar o emprestimo bancario para a compra de uma casa
# o programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS  ele vai pagar.
# calcule o valor da prestação mensal, sabendo que ela não pode
# exceder 30% do salario ou então o emprestimo será negado
print('===============================')
print('====Aprovador de Emprestimo====')
print('===============================')
valor_casa = float(input('Digite o valor da casa:'))
salario = float(input('Digite o seu salrio:'))
meses = int(input('Digite em quantos meses será parcelada:'))
mensalidade = valor_casa // meses
credito = (30 * salario) / 100
print(f'O Valor da casa é:"R${valor_casa}"')
print(f'O Seu salario é:"R${salario}"\nE o valor referente a 30% do mesmo é:"R${credito}"')
print(f'Já o valor das parcelas ficaram em R$"{mensalidade}"')
if mensalidade <= credito:
    print('Por isso seu emprestimo foi APROVADO')
else:
    print('Por isso seu emprestimo foi NEGADO')
