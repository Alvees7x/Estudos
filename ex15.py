# Aluguel de carros

def aluguel_carros():
    print('LOCADORA DE VEÍCULOS')
    print('~' * 20)
    km = float(0.15)
    valor_dias = int(60)
    qt_km = float(input('Quantos KM foram rodados?: '))
    qt_dias = int(input('Quantos dias foram alugados?: '))
    total_conta = (qt_dias * valor_dias) + ( qt_km * km)
    print(f'Você deverá pagar R${total_conta} por {qt_dias} dias alugados e {qt_km}Km rodados.')







aluguel_carros()
