# Calculo de tinta para a área de uma parede

def calcular_tinta():
    largura = float(input('Qual a largura da parede em metros?: '))
    altura = float(input('Qual a altura da parede em metros?: '))
    area = largura * altura
    tinta_necessaria = area / 2 # Cada litro de tinta cobre 2 metros quadrados
    print(f'A área da parede é de {area:.2f} metros quadrados.'
          f'\nVocê precisará de {tinta_necessaria:.2f} litros de tinta.', end='')

calcular_tinta()