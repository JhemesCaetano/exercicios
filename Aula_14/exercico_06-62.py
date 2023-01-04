# melhore o desafio 61. perguntando para o usúario se ele quer  mostrar alguns termos.
# o programa acaba quando ele dizer que não quer mais ver nenhum termo
t = int(input("Digite o primeiro termo da PA:"))
r = int(input('Digite a Razão da PA:'))
final = ''
pa = t - r
z = 0
while final != 'n':
    pa += r
    print(pa)
    z += 1
    if z == 10:
        final = str(input('''Quer ver mais termos da PA [s/n]''')).strip().lower()

        if final != 's' and final != 'n':
         print('Desculpa, mas essa opção é invalida')
         break
        if final == 's':
           z = 11 - int(input('Quantos termos a mais você gostaria de ver?:'))
           pa += r
           print(pa)
print("até mais..")
