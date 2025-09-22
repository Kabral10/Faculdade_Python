#Passo 1 -> Criar funções e importar bib's
def leiaint(msg):
    while True:
        try:
            numero = int(input(msg))
        except ValueError: #Se não converter para int
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        else:
            return numero
def linha():
    print('-=' * 30)

linha()
n = leiaint('Digite um numero: ')
print(f'Você digitou o numero: {n}')
linha()
