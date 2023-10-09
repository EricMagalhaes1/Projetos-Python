menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""


saldo = 0
limite = 1000
extrato =''
qtd_saques = 0
nmr_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input('Informe o valor a ser depositado: '))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}"

        else:
            print('Operação invalida')
    
    elif opcao =='s':
            
        valor = float(input('Informe o valor a ser sacado: '))
            
        verificar_saldo = valor > saldo
            
        verificar_limite = valor > limite

        verificar_saque = nmr_saques > LIMITE_SAQUE


        if verificar_saldo:
                print('Saldo Insuficiente.')
            
        elif verificar_limite:
                print('Valor ultrapassou o limite.')

        elif verificar_saque:
                print("Limite de saques exedido")
            
        elif valor > 0:
                saldo -= valor
                nmr_saques =+1
                extrato +=  f"Saque: R$ {valor:.2f}"
                
        else:
            print('Valor invalido.')
        
    elif opcao == 'e':
        print(saldo)
          
    elif opcao =='q':
        quit
    
    else:
        print("Operação invalida")
        
