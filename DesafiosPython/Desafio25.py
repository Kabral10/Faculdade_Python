#Crie um programa que leia 3 numeros e retorne qual o maior e qual o menor

#introdução
print('--- Maior ou Menor ---')

#inserção de dados
n1 = int(input('Qual o primeiro numero:\n'))
n2 = int(input('Qual o segundo numero:\n'))
n3 = int(input('Qual o terceiro numero:\n'))

#Funções
def verifica_maior(a,b,c):
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    print(f'\n{maior} é o maior numero!')

def verifica_menor(a,b,c):
    menor = a
    if b < menor:
        menor = b
    if c < menor:
        menor = c
    print(f'{menor} é o menor numero!\n')

#Exibição
verifica_maior(n1,n2,n3)
verifica_menor(n1,n2,n3)