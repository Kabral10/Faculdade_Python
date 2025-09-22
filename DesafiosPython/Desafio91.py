#Passo 1-> Importar Bibliotecas
import time

#Passo 2-> definir funções
def contador(a, b ,c):
    for i in range(a, b, c):
        print(f'{i} ', end='')
        time.sleep(0.7)
    print('FIM!')

def linha():
    time.sleep(0.7)
    print('~' * 20)

#Passo 3-> definir os parametros
linha()
print('Contagem de 1 até 10 de 1 em 1')

contador(1,11,1)
linha()

linha()
print('Contagem de 10 até 0 de 2 em 2')

contador(10,-1,-2)
linha()

linha()
print(f'Agora é sua vez!')
a = int(input(f'Início: '))
b = int(input(f'Fim: '))
c = int(input(f'Metodo: '))
linha()
print(f'Contagem de {a} até {b} de {c} em {c}')
contador(a,b+1,c)
linha()
