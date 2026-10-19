nome = str(input("Digite seu nome: "))

print(f'O tipo primitivo desse valor é {type(nome)}')
if nome.istitle():
    print("Seu nome começa com letra maiúscula")
else:
    print("Seu nome não começa com letra maiúscula")
    