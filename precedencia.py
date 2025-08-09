# Precedência de Operadores em Python (do mais prioritário para o menos)
# 1. Parênteses: ( )          -> força a avaliação primeiro
# 2. Exponenciação: **        -> potência (2 ** 3 = 8)
# 3. Sinais unários: +x, -x   -> positivo ou negativo
# 4. Multiplicação, Divisão, Módulo e Floor division: *, /, %, // da esquerda para a direita
# 5. Adição e Subtração: +, -
# 6. Operadores de comparação: ==, !=, >, <, >=, <=
# 7. Operadores lógicos: not, and, or

# Exemplo:
# resultado = 2 + 3 * 4  # Multiplicação antes da soma, resultado é 14
# resultado = (2 + 3) * 4 # Parênteses primeiro, resultado é 20
print(10-5*2)