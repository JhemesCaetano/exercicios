'''
    Sistema Bancário com python , exercicio da DIO Bootcamp:
        Potência Tech powered by iFood | Ciências de Dados com Python
    Nesse sistema Bancário teremos:
        Operação de depósito:
            Deve ser possível depositar valores positivos para a minha conta bancária.
            A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos
            nos preocupar em identificar qual é o número da agência e conta bancária.
            Todos os depósitos devem ser armazenados em uma variável e exibidos na
        Operação de saque:
            O sistema deve permitir realizar 3 saques diários com limite máximo de R$500,0
            por saque. Caso o usuário não tenha saldo em conta o sitema deve ixibir uma
            mensagem informando que não será possível sacar o dinheiro por falta de saldo.
            Todos os saques devem ser armazenados em uma variável e exibidosna operação de extrato
        Operação de extrato:
            Essa operação deve listar todos os depósitos e saques realizados na conta.
            No fim da listagem deve ser exibido o saldo atual da conta.
            Os valores devem ser exibidos utilizando o formato R$xxx.xx
            exemplo:
            1500.45 = R$1500.45
        Criação de usuário:
            Essa função cria um usuario com Nome, Data de Nascimento, Endereço e CPF.
            Só é permitido criar um usuario por CPF, caso contrario retorna um erro
        Criação de Contas:
            Essa função  cria uma conta com base nos CPF's cadastrados, sendo possivel criar quantas
            contas quise.
        Listar Contas:
            Essa função listas as contas criadas por CPF's:

        
        

        

'''

saldo = 0
depositos = []
saques = []
opcao = 0
QTD_SAQUE_DIA = 3
usuarios = []
contas = []


def criar_usuario(nome, data_nascimento, endereco, cpf):
    # Verifica se o CPF já existe na lista
    for usuario in usuarios:
        if usuario['CPF'] == cpf:
            print(f"CPF {cpf} já cadastrado. Não é possível adicionar o usuário.")
            return

    # Cria um dicionário com as informações do usuário
    novo_usuario = {
        'Nome': nome,
        'Data de Nascimento': data_nascimento,
        'Endereço': endereco,
        'CPF': cpf
    }

    # Adiciona o novo usuário à lista
    usuarios.append(novo_usuario)
    print(f"Usuário {nome} adicionado com sucesso.")

def criar_conta(cpf):
    # Filtra a lista de usuários pelo CPF
    usuario_filtrado = list(filter(lambda usuario: usuario['CPF'] == cpf, usuarios))

    # Verifica se o usuário existe na lista
    if not usuario_filtrado:
        print("Usuário não encontrado.")
        return

    # Verifica o próximo número da conta sequencial
    numero_conta = len(contas) + 1

    # Cria um dicionário com os dados da conta
    nova_conta = {
        'Agência': '0001',
        'Número da Conta': str(numero_conta),
        'Usuário': usuario_filtrado[0]
    }

    # Adiciona a nova conta à lista de contas
    contas.append(nova_conta)
    print(f"Conta {numero_conta} criada para o usuário {usuario_filtrado[0]['Nome']}.")

def extrato(saldo, /, *, saques, depositos, ):
    #Verifica o seus ultimos saques, depósitos e o seu saldo
    print(f"==========EXTRATO==========\n"
          f"ULTIMOS DEPOSITOS:{depositos}\n"
          f"ULTIMOS SAQUES:{saques}\n"
          f"\n"
          f"SALDO ATUAL:R${saldo:.2f}\n"
          f"{'='*28}")

def sacar(*,saque, saldo, saques, qtd_saque_dia):
    if saldo >= saque and saque <= 500:
        saldo -= saque
        saques.append(f'R$ {saque:.2f}')
        print(f'Vocẽ Efetuou um Saque no Valor de: (R$ {saque:.2f})')
        qtd_saque_dia -= 1
    elif saldo < saque and saque <= 500:
        print(f'Desculpa seu Saldo é Insuficiente')
    elif saque > 500:
        print('Desculpe mas só é permitido sacar até R$500.0')
    if qtd_saque_dia == 0:
        print('Desculpe mas Vocẽ exedeu a quantidade de saque permitido para o dia de hoje')
    else:
        print(F'Você ainda tem "{qtd_saque_dia}" saques disponivel durante o dia de hoje')
    return saldo, saques
def depositar(saldo, depositos, valor, /):
    if valor > 0:
        saldo += valor
        depositos.append(f'R$ {valor:.2f}')
        print(f'Você Efetuou um deposito de: (R$ {valor:.2f})')
    else:
        print('Operação falhou! O valor informado é invalido.')
    return saldo, depositos

while True:
    print(f'''Bem vindo ao Menu do Banco
        Opções:
            1-Extrato
            2-Sacar
            3-Depositar
            4-Criar usuário
            5-Criar Conta
            6-Sair
        ''')
    # Escolhe uma das opções do Menu:
    try:
        opcao = int(input('Por favor Digite o Número da opção desejada:'))
        if opcao <= 0 or opcao > 8:
            print('Por favor Digite uma opção valida')
    except ValueError:
        print('Por favor Digite uma opção valida')
    # Chama a função Extrato:
    if opcao == 1:
       saldo = extrato(saldo, saques= saques, depositos= depositos)
    # Chama a função Sacar:3
    elif opcao == 2:
        print('''Sistema De Saque:
           Vocẽ pode efetuar até 3 saques diarios , com um limite de  R$500.0 cada''')
        try:
            saque = float(input("Por Favor Digite o Valor a ser Sacado:"))
        except ValueError:
            print('Por Favor Digite um Valor Valido...')

        saldo, saques = sacar(saque= saque, saldo= saldo, saques= saques, qtd_saque_dia= QTD_SAQUE_DIA,)
    elif opcao == 3:
        valor = float(input('Digite o Valor a ser Depósitado:'))
        saldo, depositos, = depositar(saldo, depositos, valor)
    elif opcao == 4:
        criar_usuario(
            input(str('Informe o seu Nome:')),
            input(str(' Informe sua Data de Nascimento, dd/mm/aa:')),
            input(str('Informe o seu Endereço; Cidade, Bairro, Rua, Número:')),
            input((str('CPF:')))
        )
    elif opcao == 5:
        criar_conta(
            input(str('Digite o numero do seu CPF:'))
        )
    elif opcao == 6:
        break
