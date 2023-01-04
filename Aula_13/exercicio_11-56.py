# desenvolva um programa que leia o NOME, IDADE E O SEXO  de 4 pessoas. no final do programa mostre:
# A media  de idade do grupo
# qual é o nome do homem  mais velho
# quantas mulheres tem menos de 20 anos
soma_das_idades = 0
media_das_idades = 0
maior_idade_homem = 0
nome_do_mais_velho = 0
for pessoas in range(1, 5):
    print(f"-=-=-=-={pessoas}ª Pessoa-=-=-=-=")
    nome = str(input("Nome:")).strip()
    idade = int(input("Idade:"))
    sexo = str(input('Sexo:[M/F)]:')).strip().lower()
    soma_das_idades += idade
    totmulher20 = 0
    if  pessoas == 1 and sexo in 'm':
        maior_idade_homem = idade
        nome_do_mais_velho = nome
    if sexo in 'm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_do_mais_velho = nome
    if sexo in 'f' and idade < 20:
        totmulher20 += 1
media_das_idades = soma_das_idades // 4
print(f'A media de idade do grupo é:"{media_das_idades}."')
print(f'O "{nome_do_mais_velho}" é o homem mais velho do grupo com, "{maior_idade_homem}"anos de idade.')
print(f'Ao todo tem "{totmulher20}" mulher(es) com menos de 20 anos')
