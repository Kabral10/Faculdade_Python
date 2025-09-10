import random
tupla = random.sample(range(1, 100), 5)

for i in tupla:
    print(i)

print(f'\nO maior numero da tupla é {max(tupla)}')
print(f'O maior numero da tupla é {min(tupla)}')