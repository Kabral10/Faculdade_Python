#Passo 1 -> Criar as funções e importar bib's
def fatorial(num, show=False):
    '''
    ---> Faz a conta de um numero selecionado exibindo seu fatorial
    :param num: Define o numero que você deseja fatorar
    :param show: Por padrão vem como False. [Caso True, retorna o calculo além do resultado]
    :return: O valor do fatorial de num
    '''
    f = 1
    for n in range(num, 0, -1):
        f *= n
        if show:
            print(n, end=' ')
            if n > 1:
                print(' x ', end=' ')
            else:
                print(' = ', end=' ')
    return f
def linha():
    print('-=' * 30)

linha()
help(fatorial)
linha()
print(fatorial(5, True)) # Mostra o processo!
linha()
print(fatorial(5)) # Não mostra o processo
linha()