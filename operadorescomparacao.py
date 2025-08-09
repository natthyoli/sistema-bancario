saldo=450
saque=200
print(saldo==saque)
saldo=600
saque=150
print(saldo!=saque)
Luz_acesa = True
precisa_apagar = True
print(f"Luz acesa: {Luz_acesa}, Precisa apagar? {precisa_apagar}")
salario = int(input('Digite o seu salário: '))

if salario <= 2000:
    print('conta clt')
else:
    print('conta pj')
    renda_mensal = int(input("Digite o valor da sua renda mensal: "))
filhos = int(input("Digite a quantidade de filhos: "))
idade_mae = int(input("Digite a idade da mãe: "))

direito_beneficio = (renda_mensal <= 1500) and (filhos >= 1) and (idade_mae >= 18)

if direito_beneficio:
    print('Você tem direito ao benefício')
else:
    print('Não atende aos requisitos')