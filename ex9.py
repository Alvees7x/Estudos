# Tabuada

def tabuada(n):
    print(f'Tabuada do {n}:')
    for i in range(1, 11):
        resultado = n * i
        print(f'{n} x {i} = {resultado}')

tabuada(7)
