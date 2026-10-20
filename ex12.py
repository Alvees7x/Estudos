# Sistema de desconto


def calcular_desconto():
    print('SISTEMA DE DESCONTO')
    desconto = float(input('Qual o valor do desconto?: '))
    preco =  float(input('Qual o preço do produto?: '))
    preco_final = preco - (preco * desconto / 100)
    print(f'O valor do produto com desconto é de R${preco_final:.2f}')

calcular_desconto()
