menu = """

[d] = Depositar
[s] = Sacar
[e] = Extrato
[q] = sair

=> """

saldo = 0
limite = 500
numero_de_saque = 0
LIMITE_DE_SAQUE = 3
extrato = ""

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("valor de Deposito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print("Deposito realizado, obrigado por ser nosso cliente!")
        else:
            print("Falha na operação, valor invalido!")

    
    elif opcao == "s":
        valor = float(input("Bem vindo, por favor informe o valor do saque"))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_de_saque >= LIMITE_DE_SAQUE
       
        if excedeu_saldo:
            print("Saldo insuficiente, verifique novamente")
            extrato += f"tentativa de saque sem saldo\n"
       
        elif excedeu_limite:
            print("Limite excedido!")
            extrato += f"Tentativa de saque acima do limite permitido\n"

        elif excedeu_saques:
            print("Limite de saques atingido")
            extrato += f"Tentativa de saques com limite de saque atingido\n"

        elif valor > 0:
            saldo-= valor
            extrato+= f"Saque realizado: R$ {valor:.2f}\n"
            numero_de_saque += 1
            print("Saque realizado, obrigado por ser nosso cliente!")


    elif opcao == "e":
        print("##########EXTRATO##########")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("############################")

    elif opcao == "q":
        print("Tenha um Bom Dia")

        break


    else:
        print("operação invalida, por favor selecione novamente a operação desejada")

    
