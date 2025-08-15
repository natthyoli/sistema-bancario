def mostraLinha():
    print("_______________________________________________________________")

SALDO = 2000
LIMITE = 500
LIMITE_SAQUES = 3
EXTRATO = ""
VALOR_SAQUE_LIMITE = 1500  
VALOR_DEPOSITO = 0.0       

while True:
    print("\nBem-vindo ao Banco Winona :")
    print("[1] Saque")
    print("[2] Depósito")
    print("[3] Extrato")
    print("[0] Sair")
    mostraLinha()

    opcao = input("Digite uma opção (ou -1 para sair): ").strip()

    if opcao == "0" or opcao == "-1":
        print("Saindo do sistema")
        break

    # Saque
    if opcao == "1":
        if LIMITE_SAQUES > 0:
            saque = float(input("Digite o valor do saque: "))

            if saque <= SALDO:
                SALDO -= saque
                LIMITE_SAQUES -= 1
                print(f"Você sacou R$ {saque:.2f}. Saldo atual: R$ {SALDO:.2f}")
                print(f"Você fez {3 - LIMITE_SAQUES} saque(s).")

            elif saque <= VALOR_SAQUE_LIMITE:
                VALOR_SAQUE_LIMITE -= saque
                LIMITE_SAQUES -= 1
                print(f"Você utilizou R$ {saque:.2f} do limite.")
                print(f"Limite restante: R$ {VALOR_SAQUE_LIMITE:.2f}")
                print(f"Você fez {3 - LIMITE_SAQUES} saque(s).")

            else:
                print("Saldo e limite insuficientes para saque.")
        else:
            print("Número de saques excedido.")

    
    elif opcao == "2":
        deposito = float(input("Digite um valor para depositar: "))
        if deposito > 0:
            SALDO += deposito
            VALOR_DEPOSITO += deposito
            print(f"Você depositou R$ {deposito:.2f}. Saldo atual: R$ {SALDO:.2f}")
        else:
            print("Valor de depósito inválido.")

    
    elif opcao == "3":
        print(f"Saldo atual: R$ {SALDO:.2f}")
        print(f"Limite disponível: R$ {VALOR_SAQUE_LIMITE:.2f}")
        print(f"Total depositado: R$ {VALOR_DEPOSITO:.2f}")
