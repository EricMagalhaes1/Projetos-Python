def menu():
    menu = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [lc] Listar Contas
        [nc] Nova Conta
        [nu] Novo Usuario
        [q] Sair
    =>"""
    return input(menu)


def deposito(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito realizado no valor de R$: {valor:.2f}\n"
        print("Deposito realizado com sucesso!")
    else:
        print("Valor invalido!")

    return saldo, extrato


def saque(*, saldo, valor, extrato, nmr_saques, LIMITE_SAQUE, limite):
    verificar_saldo = valor > float(saldo)
    verificar_limite = valor > limite
    verificar_saque = nmr_saques >= LIMITE_SAQUE

    if verificar_saldo:
        print('Saldo Insuficiente.')
    elif verificar_limite:
        print('Valor ultrapassou o limite.')
    elif verificar_saque:
        print("Limite de saques exedido")
    elif valor > 0:
        saldo -= valor
        nmr_saques += 1
        extrato += f"Saque realizado no valor de R$: {valor:.2f}"
    else:
        print("Valor Invalido!")

    return extrato, saldo


def exibir_extrato(extrato, saldo):
    print("===================Extrato===================")
    print("Nenhuma movimentação foi realizada" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo}")
    print("==============================================")


def criar_usuarios(usuarios):
    cpf = input('Informe o CPF: ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Já existe um usuario cadastrado com esse CPF")
        return

    nome = input('informe seu nome: ')
    dt_nacimento = input('Informe sua data de nascimento: ')
    endereco = input('Informe seu endereço completo: ')

    usuarios.append({'nome': nome, 'dt_nascimento': dt_nacimento, 'cpf': cpf, 'endereco': endereco})

    print('Usuario criado com sucesso!')


def filtrar_usuarios(cpf, usuarios):
    filtro = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return filtro[0] if filtro else None


def criar_conta(agencia, nmr_conta, usuarios):
    cpf = input("Insira seu CPF: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print('Conta criada com sucesso')
        return {'agencia': agencia, 'nmr_conta': nmr_conta, 'usuario': usuario}

    print('usuario não encontrado')


def main():
    LIMITE_SAQUE = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 1000
    extrato = ''
    qtd_saques = 0
    nmr_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input('Informe o valor a ser depositado: '))
            saldo, extrato = deposito(saldo=saldo, valor=valor, extrato=extrato)

        elif opcao == 's':
            valor = float(input('Informe o valor a ser sacado: '))
            saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato, nmr_saques=nmr_saques,
                                   LIMITE_SAQUE=LIMITE_SAQUE, limite=limite)

        elif opcao == 'e':
            exibir_extrato(saldo,extrato)

        elif opcao == 'nu':
            criar_usuarios(usuarios=usuarios)

        elif opcao == 'nc':
            nmr_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, nmr_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == 'lc':
            pass


main()
