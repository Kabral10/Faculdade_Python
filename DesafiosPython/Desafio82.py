lista = []
escolha = 'S'
while escolha == 'S':
    nome = input('Digite seu nome: ').title().strip()
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    escolha = input('Deseja continuar? [S/N] ').upper().strip()
    if escolha == 'N':
        break
print('\n='+'-='*19)

print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, aluno in enumerate(lista):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

print('='+'-='*19)

while True:
    opc = int(input('Deseja ver qual nota? [999 finaliza] '))
    if opc == 999:
        print('Finalizando...')
        break
    if 0 <= opc <= len(lista):
        print(f'As notas de {lista[opc][0]} são: {lista[opc][1]}')