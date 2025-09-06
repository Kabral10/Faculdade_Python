n = int(input('Digite um número: '))

mult = 0
for i in range(2, int(n**0.5) + 1):
    if (n % i == 0):
        mult += 1

if (mult == 0):
    print(f'O número {n} é primo')
else:
    print(f'O número {n} não é primo')