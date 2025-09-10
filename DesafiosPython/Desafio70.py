palavras = (input('Digite uma palavra: '),
            input('Digite uma palavra: '),
            input('Digite uma palavra: '),
            input('Digite uma palavra: '))

for i in palavras:
    if 'a' or 'e' or 'i' or 'o' or 'u' in i:
        print('---------------------')
        print(i)
        print(f'Existe(m) {i.count('a')} vogal(is) (a)')
        print(f'Existe(m) {i.count('e')} vogal(is) (e)')
        print(f'Existe(m) {i.count('i')} vogal(is) (i)')
        print(f'Existe(m) {i.count('o')} vogal(is) (o)')
        print(f'Existe(m) {i.count('u')} vogal(is) (u)')
        print('---------------------')
    else:
        print(f'{i} não tem vogais!')