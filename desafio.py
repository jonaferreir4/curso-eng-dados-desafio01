menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def depositar ():
    global saldo, extrato
    while True:

        valor = float(input("digite o valor que deseja depositar: "))
        if valor <= 0:
            print("O valor tem que ser positivo e não nulo!")
        else:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Valor depositado com sucesso!")
            break
    return

def sacar ():
    global limite, saldo,extrato,  numero_saques, LIMITE_SAQUES
    while True:
        valor = float(input("digite o valor que deseja sacar: "))
        
        if valor > limite:
            print(f"O limite é R$ {limite},00 por saque!")
            break
        elif saldo == 0: 
            print ("Você está sem saldo!")
            break
        elif valor > saldo:
            print(f"Saldo insuficente para concuir a operação! Seu saldo é de R${saldo},00")
            break
        elif numero_saques == LIMITE_SAQUES:
            print("Você atingiu o limite de saques")
            break
        else:
            saldo -= valor
            print("Valor sacado com sucesso")
            numero_saques = numero_saques + 1
            extrato += f"saque: R${valor:.2f}\n"
            break
    return

def extratoConta():
    global extrato, saldo
    print(extrato)
    print(f"Total: R$ {saldo:.2f}")



while True:
    opcao = input(menu)
    
    if opcao == 'd':
        depositar()
    elif opcao == 's':
        sacar()
    elif opcao == 'e':
        extratoConta()
    elif opcao == 'q':
        break
    else: 
        print("opção inválida!")