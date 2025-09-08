print('=-=-=-=-=-=--=-=-=-=-=-=-=')
print('|Banco de dados iniciante|')
print('=-=-=-=-=-=--=-=-=-=-=-=-=\n')

#Contagens
idade18 = 0
homens = 0
mulher20 = 0

#inicializador
escolha = 'S'

while escolha == 'S':
    if escolha == 'S':
        print('=-=-=-=-=-==-=-=-=-=-=')
        print('| Cadastro de Pessoa |')
        print('=-=-=-=-=-==-=-=-=-=-=')

        sexo = str(input('Sexo [M/F]: ')).upper().strip()
        while sexo != 'M' and sexo != 'F':
            sexo = str(input('Sexo [M/F]: ')).upper().strip()

        idade = int(input('Idade: '))
        while idade < 0:
            idade = int(input('Idade: '))

        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulher20 += 1
        if idade > 18:
            idade18 += 1

        escolha = str(input('\nDeseja cadastrar mais uma pessoa? [S/N]: ')).upper().strip()

    if escolha == 'N':
        print('===== RESULTADO =====')
        print(f'O total de pessoas com mais de 18 anos: {idade18}')
        print(f'Ao todo temos {homens} homens cadastrados')
        print(f'E temos {mulher20} mulheres com menos de 20 anos')
        print('Encerrando o programa...')
        print('=====================')
        break


