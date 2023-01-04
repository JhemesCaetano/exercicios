# refaça o exercico dos triangulos acresentando o recurso de mostrar que tipo de tringulo será formado:
# equilátero: todos os lados são iguais
# isósceles: dois lados iguais
# escaleno todos os lados diferentes
def blocox():
    if reta1 == reta2 == reta3:
        print('Esse triangulo é um: "Equilátero"')

    elif reta1 == reta2 != reta3 or reta1 == reta3 != reta2 or reta2 == reta3 != reta1:
        print('Esse triangulo é um: "Isóceles"')

    elif reta1 != reta2 != reta3:
        print('Esse triangulo é um: "Escaleno"')


while True:
    reta1 = float(input('Digite a primeira reta:'))
    reta2 = float(input('Digite a segunda reta:'))
    reta3 = float(input('Digite a terceira reta:'))
    if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
        blocox()
    else:
        print('Não é possivel criar um triangulo com essas retas.\nO programa será finalizado...')
        break
