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
'''
saldo = float(1000)
depositos = []
saques = []
opcao = 0
qtd_saque_dia = 3
def extrato():
    global saldo
    global saques
    global depositos
    print(f'''
        Seus Ultimos Depósitos Foram: {depositos}
        
        Seus Ultimos Saques Foram: {saques}
        
        Seu Saldo Atual é: (R$ {saldo:.2f})''')

def sacar():
    global saldo
    global saques
    global qtd_saque_dia
    print('''Sistema De Saque:
    Vocẽ pode efetuar até 3 saques diarios , com um limite de  R$500.0 cada''')
    try:
        saque = float(input("Por Favor Digite o Valor a ser Sacado:"))
    except ValueError:
        print('Por Favor Digite um Valor Valido...')
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
def depositar():
    global saldo
    global depositos
    deposito = float(input('Digite o Valor a ser Depósitado:'))
    saldo += deposito
    depositos.append(f'R$ {deposito:.2f}')
    print(f'Você Efetuou um deposito de: (R$ {deposito:.2f})')

while True:
    print(f'''Bem vindo ao Menu do Banco
        Opções:
            1-Extrato
            2-Sacar
            3-Depositar
            4-Sair
        ''')
    try:
        opcao = int(input('Por favor Digite o Número da opção desejada:'))
        if opcao <= 0 or opcao > 4:
            print('Por favor Digite uma opção valida')
    except ValueError:
        print('Por favor Digite uma opção valida')
    if opcao == 1:
        extrato()
    elif opcao == 2:
        sacar()
    elif opcao == 3:
        depositar()
    elif opcao == 4:
        break
