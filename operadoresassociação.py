# Operadores de associação em Python verificam se um valor está (ou não está) presente em uma sequência (como listas, strings, tuplas...)

# Temos dois operadores principais:
# 1. 'in'     -> Retorna True se o valor estiver na sequência
# 2. 'not in' -> Retorna True se o valor NÃO estiver na sequência

# Exemplos práticos:

print('banana' in frutas)     # True, porque 'banana' tá na lista
print('uva' not in frutas)    # True, porque 'uva' não tá na lista

# Funciona com strings também"
#mensagem = "Aprendendo Python é top!"
print('Python' in mensagem)   # True, porque a palavra tá dentro da string

###########################################################################################

# Listas de alunos aprovados e reprovados
nomes_alunos_aprovados = ['Alicia', 'Aline', 'Alissa', 'Alessandra', 'Bruna', 'Barbara', 'Caroline', 'Cristina', 'Deyse']
nomes_alunos_reprovados = ['Andressa', 'Anitta', 'Cleo', 'Dora', 'Fatima', 'Juliana', 'Marcelly', 'Saulo']

# Nome que você quer verificar
nome = input("Digite o nome do aluno: ")

# Verificação
if nome in nomes_alunos_aprovados:
    print(f'{nome} foi aprovada!')
elif nome in nomes_alunos_reprovados:
    print(f'{nome} foi reprovada.')
else:
    print(f'{nome} não está na lista de alunos.')
 #####
produtos = {
    1: ('leite', 5.60),
    2: ('bolo', 25.00),
    3: ('pão', 11.00),
    4: ('oleo', 10.00),
    5: ('sabão em pó', 210.00)
}

print("Menu de produtos:")
for numero, (nome, preco) in produtos.items():
    print(f"{numero} - {nome.capitalize()} - R$ {preco:.2f}")

escolha = int(input("Escolha o número do produto: "))

if escolha in produtos:
    nome, preco = produtos[escolha]
    quantidade = int(input(f'Digite a quantidade de {nome}: '))
    valor_compra = preco * quantidade
    print(f'Você escolheu {nome.capitalize()}, quantidade: {quantidade}')
    print(f'O valor da compra é R$ {valor_compra:.2f}')
else:
    print("Produto inválido. Tente novamente.")


 
