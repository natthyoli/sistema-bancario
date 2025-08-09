# Estruturas condicionais em Python servem para executar blocos de código diferentes
# dependendo se uma condição é verdadeira ou falsa.

# A estrutura básica é o "if", que verifica uma condição:
# if condição:
#     bloco de código executado se a condição for True

# Podemos usar "else" para executar outro bloco caso a condição seja False:
# if condição:
#     bloco se True
# else:
#     bloco se False

# Também existe "elif" (else if), para verificar múltiplas condições em sequência:
# if condição1:
#     bloco 1
# elif condição2:
#     bloco 2
# else:
#     bloco padrão caso nenhuma condição anterior seja True

# As condições geralmente comparam valores usando operadores como ==, !=, >, <, >=, <=
# e podem combinar múltiplas condições com "and", "or", "not".
idade = int(input('Digite a sua idade: '))
if idade >= 18:
    print('Você está apto(a) para tirar carteira de habilitação.')
else:
    print('Você é menor de idade.')

    saldo=2000.0
    saque=float(input("Informe o valor do saque:"))
    if saldo>=saque:
        print("Realizando saque!")

    if saldo <=saque:
        print("Saldo insuficiente")    

        import sys
opcao = int(input("Informe uma opção:\n[1] Saque\n[2] Extrato\nOpção: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
    print(f"Você escolheu sacar R$ {valor:.2f}")
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    sys.exit("Opção inválida. Encerrando o programa.")
MAIOR_IDADE=18 
IDADE_ESPECIAL=17
idade=int(input("Digite a sua idade : "))
if (idade==MAIOR_IDADE):
   print("Esta apto(a)dirigir") 
elif(idade==IDADE_ESPECIAL):
    print("Pode fazer somente as aulas teoricas")
else:
    print("Sua idade não atende aos critérios da CNH")