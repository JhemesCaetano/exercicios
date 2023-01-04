# escreva um programa que leia 3 comprimentos de retas , e fala ao usuario se elas podem ou não montar um triangulo
reta1 = int(input('Comprimento da primeira reta:'))
reta2 = int(input('Comprimento da segunda reta:'))
reta3 = int(input('Comprimento da terceira reta:'))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print(f'É possivel criar um traingulo com essas retas: "{reta1}", "{reta2}", "{reta3}"')
else:
    print(f"Não é possivel criar um triangulo com essas retas: '{reta1}', '{reta2}', '{reta3}'")


