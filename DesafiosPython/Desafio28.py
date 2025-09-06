#Escreva um programa para aprovar um imprestimo bancario para a compra de uma casa. O programa vai perguntar ( o valor da casa , o salario do comprador , e quantos anos de financiamento )
#Calcule o valor da prestação mensal ( Sabendo que não pode exceder 30% do salario ) ou então se o emprestimo será negado

ValorDaCasa = float(input("Qual é o valor da casa que você deseja comprar? R$"))
Salario = float(input("Qual é o seu salário? R$"))
Anos = int(input("Em quantos anos você deseja pagar? "))

if Anos <= 0:
    print("Número de anos inválido. Por favor, insira um valor maior que zero.")
else:
    if Salario > 0:
        Prestacao = ValorDaCasa / (Anos * 12)
        if Prestacao > 0.3 * Salario:
            print("Empréstimo negado. A prestação mensal não pode exceder 30% do salário.")
        else:
            print("Empréstimo aprovado. A prestação mensal será de R${:.2f}".format(Prestacao))
    else:
        print("Salário inválido. Por favor, insira um valor maior que zero.")