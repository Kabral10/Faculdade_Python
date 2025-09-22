#Passo 1 -> Definir funções e variaveis
import time
def maior(*num):
    if len(num) == 0:
        print('Nenhum valor foi informado')
        return
    maiorvalor = num[0]
    for i in num:
        if i > maiorvalor:
            maiorvalor = i

    print(f'Analisando os valores passados...')
    for n in num:
        time.sleep(0.5)
        print(f'{n} ', end='')

    time.sleep(0.5)
    print(f'- Foram informados {len(num)} valores ao todo!')

    time.sleep(0.5)
    print(f'O maior valor informado foi {maiorvalor}')
def linha():
    print('-=' * 20)

#Passo 2 -> Receber parâmetros e Exibir
linha()
maior(10,20,30,40,999)
linha()
maior(10,1,20,31,231,918,1000)
linha()
