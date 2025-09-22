#Passo 1-> Definir a função secreva()
def escreva(txt):
    tamanho = len(txt)
    print('~'*(tamanho + 2))
    print(f' {txt}')
    print('~'*(tamanho + 2))

#Passo 2-> Receber um texto como parametro da função e exibir uma mensagem com tamanho adapptavel
texto = input('Qual o seu texto? ')

#Passo 3-> Exibir o resultado
escreva(texto)
