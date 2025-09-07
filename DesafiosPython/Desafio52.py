p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
contador = 1
total = 10
mais = 1

while mais != 0:
    while contador <= total:
        termo = p + (contador-1)*r
        print(f'{contador}ª termo: {termo}')
        contador += 1
    print('Pausa')
    mais = int(input('Quantos numeros a mais deseja mostrar?'))
    total += mais

print('Saindo do programa...\nObrigado por utilizar o sistema!')