# Operadores aritméticos

#Adição: +
#Subtração: -
#Multiplicação: *
#Divisão: /
#Divisão inteira: //
#Exponenciação: **
#Módulo: % = resto da divisão
#Igualdade: ==

# Comparação: !=, >, <, >=, <=

#Exemplos:

def barra():
    for i in range(1, 30):
        print('-', end='')
    print()  # Imprime uma nova linha após a barra



a = 10
b = 5
c = a + b  # Adição
d = a - b  # Subtração
e = a * b  # Multiplicação
f = a / b  # Divisão
g = a // b  # Divisão inteira
h = a ** b  # Exponenciação
i = a % b  # Módulo
j = a == b  # Igualdade
k = a != b  # Comparação
l = a > b   # Maior que
m = a < b   # Menor que
n = a >= b  # Maior ou igual
o = a <= b  # Menor ou igual

barra()
print('\nOperadores Aritméticos')
print(f'\nA adição de {a} e {b} é igual a {c}\n')
print(f'A subtração de {a} e {b} é igual a {d}\n')
print(f'A multiplicação de {a} e {b} é igual a {e}\n')
print(f'A divisão de {a} e {b} é igual a {f}\n')
print(f'A divisão inteira de {a} e {b} é igual a {g}\n')
print(f'A exponenciação de {a} e {b} é igual a {h}\n')
print(f'O módulo de {a} e {b} é igual a {i}\n')
print(f'A igualdade de {a} e {b} é {j}\n')
print(f'A comparação de {a} e {b} é {k}\n')
print(f'{a} é maior que {b}? {l}\n')
print(f'{a} é menor que {b}? {m}\n')
print(f'{a} é maior ou igual a {b}? {n}\n')
print(f'{a} é menor ou igual a {b}? {o}\n')


