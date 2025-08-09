saque = float(input("Informe o valor do saque: "))
saldo = 2000
cheque_especial = 450

print("\nTipos de conta:")
print("[1] Conta Normal")
print("[2] Conta Universitária")
print("[3] Conta Especial")

tipo_conta = int(input("Escolha o tipo de conta: "))

if tipo_conta == 1:  # Conta Normal
    if saldo >= saque:
        print("Saque realizado com sucesso.")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial.")
    else:
        print("Saldo insuficiente.")

elif tipo_conta == 2:  # Conta Universitária
    if saldo >= saque:
        print("Saque realizado com sucesso.")
    else:
        print("Saldo insuficiente. Conta universitária não possui cheque especial.")

elif tipo_conta == 3:  # Conta Especial
    limite_especial = 1000
    if saldo >= saque:
        print("Saque realizado com sucesso.")
    elif saque <= (saldo + limite_especial):
        print("Saque realizado com uso do limite especial.")
    else:
        print("Saldo insuficiente.")

else:
    print("Tipo de conta inválido.")
