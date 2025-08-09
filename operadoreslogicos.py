# Operadores lógicos em Python são usados para combinar ou inverter expressões booleanas.
# Eles retornam True ou False dependendo das condições avaliadas.
# Existem três operadores principais:
# - and: retorna True se ambas as condições forem verdadeiras.
# - or: retorna True se pelo menos uma das condições for verdadeira.
# - not: inverte o valor lógico (True vira False e vice-versa).

# Exemplos:
# True and False => False
# True or False => True
# not True => False
saldo=1000
saque=200
limite=100
print(saldo >=saque)
print(saldo>=saque and saque<=limite)
print(saldo>=saque or saque<=limite)
#not
print(not 1000>1500)
saldo = 1000
saque = 200
limite = 100
conta_especial = True  # ou False, testa os dois!

resultado = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print(resultado)  # Vai imprimir True ou False conforme a lógica
