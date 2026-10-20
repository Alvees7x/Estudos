# Aumento de salário

def calcular_aumento():
    print('SISTEMA DE AUMENTO DE SALÁRIO')
    print('=' * 20)
    salario = float(input('Salario atual: R$ '))
    aumento = float(input('Qual o percentual de aumento?: '))
    salario_final = salario + (salario * aumento / 100)
    print(f'Seu novo salario com o aumento é de R${salario_final:.2f}.')
    print('=' * 20)


calcular_aumento()