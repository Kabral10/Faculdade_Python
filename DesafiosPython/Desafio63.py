frase = input('Escrava sua frase: ')

if 'A' in frase.upper():
    print(f'A sua frase tem {frase.count("a")} letras a!')
    print(f'O primeiro a está em {frase.find('a')}')
    print(f'O ultimo a está em {frase.rfind('a')}')

else:
    print('Seu texto não contem nenhuma letra a!')