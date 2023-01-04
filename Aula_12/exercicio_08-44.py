# elabore um programa que calcule o valor a ser pago por um produto o seu PREÇO NORMAL e a forma de PAGAMENTO
# a vista dinheiro/cheque:10% de desconto
# a vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal:
# 3x ou mais no cartão:20% de juros:
preco_do_produto = float(input('Digite o preço do produto:'))
desconto1 = (10 * preco_do_produto) / 100
desconto2 = (5 * preco_do_produto) / 100
acrecimo = (20 * preco_do_produto) / 100
a_vista_dinheiro = preco_do_produto - desconto1
a_vista_cartao = preco_do_produto - desconto2
tres_vezes_no_cartao = preco_do_produto + acrecimo
print(f'Seu produto a vista no dinheiro ou cheque fica no valor de:"R${a_vista_dinheiro}"')
print(f'Seu produto a vista no cartão fica no valor de:"R${a_vista_cartao}"')
print(f'seu produto em até 2x no cartão fica no valor de:"R${preco_do_produto}"')
print(f'seu produto em 3x ou mais fica no valor de:"R${tres_vezes_no_cartao}"')
