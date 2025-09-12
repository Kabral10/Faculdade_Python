parenteses = list()
expressao = str(input('Digite a sua expressao: '))

for c in range(0, len(expressao)):
    if expressao[c] == '(':
        parenteses.append('(')
    elif expressao[c] == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break

if len(parenteses) == 0:
    print('A expressao é valida!')
else:
    print('A expressao não é valida!')