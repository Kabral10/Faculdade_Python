print('Soma de numeros')

n = input('Digite um numero: ')
soma = 0

if n.isnumeric():
    n  = int(n)
    
    for i in range(1, n + 1):
        if i % 2 == 0:
            soma += i
        else:    
            pass
    print(f'A soma dos numeros é: {soma}')