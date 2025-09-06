print('---TABUADA---\n')

n = input('Deseja ver a tabuada de qual numero? ')

if(n.isnumeric() == True):
    print(f'--- Tabuada de {n} ---\n')
    n = int(n)
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')