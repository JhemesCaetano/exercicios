#crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo"
cidade = str(input('Digite o nome de uma cidade:'))
x = cidade.split()
y = x[0].lower()
if 'santos' in y:
    print('A cidade começa com "santos"')

else:
    print('A cidade não começa com "santos"')