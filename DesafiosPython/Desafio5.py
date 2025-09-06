# Crie um programa que receba um numero inteiro e retorne seu sucessor e seu antecessor

n = input('Insira um numero: ')
a = int(n)-1
s = int(n)+1

if(n.isnumeric()): 
    print(f'O numero digitado foi {n}, seu antecessor é {a} e seu sucessor é {s}')
else:
    print('Você é burrinho!')