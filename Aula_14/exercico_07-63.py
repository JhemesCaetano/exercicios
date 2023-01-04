# escreva um programa que leia 'n' inteiro e mostre na tela os "n"
# primeiros elementos de uma seguencia fibonacci
# 0 - 1 - 2 - 3 - 5 - 8
#Fn = fn-1 + Fn-2
n = int(input('Digite um numero:'))
f1 = 0
f2 = 1
fn = 0
c = 0
print(f'Os "{n}" primeiros números em uma seguencia de fibonacci são:')
while c != n:
    c += 1
    print(fn, end= ',' )
    fn = f1 + f2
    f1 = f2
    f2 = fn


