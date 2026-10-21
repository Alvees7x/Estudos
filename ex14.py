# Conversor de temperatua


conversao = input('Escolha a conversão: \n1 - Celsius para Fahrenheit \n2 - Fahrenheint para Celsius \n')

if conversao == '1':
    celsius = float(input('Digite a temperatura em Celsius: '))
    fahrenheit = (celsius * 9/5) + 32
    print(f'{celsius}°C é igual a {fahrenheit}°F')
elif conversao == '2':
    fahrenheit = float(input('Digite a temperatura em fahreinheit: '))
    celsius = (fahrenheit - 32) * 5/9
    print(f'{fahrenheit}°F é i[gual a {celsius}.')
else:
    print('Opcão inválida')
    