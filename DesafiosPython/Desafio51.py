p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
contador = 1

while contador < 10:
    termo = p + (contador-1)*r
    print(f'{contador}ª termo: {termo}')
    contador += 1