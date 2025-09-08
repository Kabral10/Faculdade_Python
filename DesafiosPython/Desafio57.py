#Loop das tabuadas
while True:
    numero = int(input('Qual tabuada deverá ser exibida? '))
    if numero < 0:
        print('Programa encerrado..')
        break

    print('-------------------------')
    for i in range(1, 10+1):
        print(f'{numero} X {i} = {numero*i}')
    print('-------------------------')
