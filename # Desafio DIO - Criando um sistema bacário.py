# Desafio DIO - Criando um sistema bacário com Python

menu = f'''
     
    ***************** BEM VINDO AO SISTENA ATM ********************
    
    [1] - Depositar 
    [2] - Sacar
    [3] - Extrato
    [4] - Sair

    ***************************************************************
'''

opcao = 0
saldo = 0
numero_saques = 0
extrato = ""
LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500.0

while opcao != 4:

    print(menu)
    opcao = int(input("    Selecione uma das opções acima: "))

    if opcao == 1:

        valor = float(input("\n    Digite o valor do deposito: "))

        if (valor < 0):
            print("\n    Valor inválido!")
        else:
            saldo += valor
            extrato += f"\n    Deposito: R$ {valor:.2f}\n"
            print("\n    Deposito realizado!")

    elif opcao == 2:

        valor = float(input("\n    Digite o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > LIMITE_VALOR_SAQUE

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\n    Saldo insuficiente!")

        elif excedeu_limite:
            print("\n    Valor do saque acima do limite!")

        elif excedeu_saques:
            print("\n    Limite de saques excedido!")

        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"\n    Saque: R$ {valor:.2f}\n"
            print("\n    Saque realizado!")
        
        else:
            print("\n    Operação falhou! O valor informado é inválido.")
        
    elif opcao == 3:
        print("\n    ***************** EXTRATO ********************")
        print("\n    Não foram realizados movimentos." if not extrato else extrato)
        print(f"\n    Saldo: R$ {saldo:.2f}")
        print("\n    **********************************************")

    elif opcao == 4:
        break

    else:
        print("\n    Operação falhou! Selecione opção válida.")

