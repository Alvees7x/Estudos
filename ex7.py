# Calculo de Média

n1 = float(input('Digite a primeira nota<: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'A sua média é {media:.2f}')


#Estrutura condicional para verificar se o aluno foi aprovado ou reprovado
if media >= 6:
    print('Você foi aprovado!')
else:
    print('Você foi reprovado!')
