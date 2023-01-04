#crie um programa que leia uma frase pelo teclado e diga:

#quatas vezes aparece a letra a

#em qual posição ela aparece a primeira vez

#em qual posição ela aparece pela ultima vez

frase = str(input('Digite uma frase:')).lower()
y = frase.replace(" ","")
quantidade = y.count('a')
começo = y.find('a')+1
final = y.rfind('a')+1
print(f'Na frase:{frase.title()}')
print(f'A letra "A" aparece em um total de: {quantidade} vezes ')
print(f'A primeira vez que ela aparece é na posição: {começo}')
print(f'E a ultima vez que ela aparece é na posição: {final}')