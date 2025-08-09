# Operadores de identidade em Python: 'is' e 'is not'
# Eles verificam se duas variáveis apontam para o MESMO objeto na memória,
# não só se os valores são iguais.
#
# Exemplo:

a = [1, 2, 3]
b = a          # b aponta para o mesmo objeto que a
c = [1, 2, 3]  # c é uma lista igual, mas objeto diferente

print(a is b)      # True, porque a e b são o MESMO objeto
print(a is c)      # False, porque a e c são objetos diferentes (mesmo valor, porém distintos)
print(a == c)      # True, porque os valores dentro das listas são iguais
print(a is not c)  # True, confirma que não são o mesmo objeto
a = [1, 2, 3]
b = a       # b aponta para o MESMO objeto que a
c = [1, 2, 3]  # c é um novo objeto com o mesmo valor

print(a is b)   # ✅ True → mesma identidade (mesmo lugar na memória)
print(a == b)   # ✅ True → mesmo valor
print(a is c)   # ❌ False → objetos diferentes na memória
print(a == c)   # ✅ True → valores iguais
