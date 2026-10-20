# Conversor de distância


def conversor_distancia():
    print('CONVERSOR DE DISTANCIA')
    print('1 - Quilometros para milhas')
    print('2 - Milhas para Quilometros')
    print('3 - Quilometros para metros')
    print('4 - Metros para Quilometros')

    opcao = int(input('Escolha uma opção: '))
    distancia = float(input('Digite uma distancia: '))


    if opcao == 1:
        resultado = distancia * 0.621371
        print(f'{distancia} km é igual a {resultado:.2f} milhas.')
    elif opcao == 2:
        resultado =  distancia / 0.621371
        print(f'{distancia} milhas é igual a {resultado:.2f} km.')
    elif opcao == 3:
        resultado = distancia * 1000
        print(f'{distancia} km é igual a {resultado:.2f} metros.')
    elif opcao == 4:
        resultado = distancia / 1000
        print(f'{distancia} metros é igual a {resultado:.2f} km.')
    else:
        print('Opção inválida!')


conversor_distancia()
