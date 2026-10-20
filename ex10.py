# Conversor de real para dolar

def conversor_real_dolar():
    print('CONVERSOR DE REAL PARA DOLAR')
    real = float(input('Digite o valor em reais (R$): '))
    dolar = real / 5.04
    print(f'R${real:.2f} é igual a ${dolar:.2f} dólares.')

conversor_real_dolar()