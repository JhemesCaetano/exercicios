#Crie um programa que pergunte a distância de uma viagem em km
#E calcule o valor da passagem, cobrando R$0,50 por km , para viagens até 200km
# e 0,45 para viagens que excedam os 200km
viagem = int(input("qual é a distancia da sua viagem em Km ?:"))
passagem1 = viagem * 0.50
passagem2 = viagem * 0.45

if viagem < 201:
    print(f"A sua viagem de {viagem}km custará R${passagem1}")
else:
    print(f"A sua viagem de {viagem}km custará R${passagem2}")
