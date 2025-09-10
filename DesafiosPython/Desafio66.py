Classificacao = ('Flamengo','Cruzeiro','Palmeiras','Bahia','Botafogo','Mirassol','São Paulo','Bragantino','Fluminense','Internacional','Ceará SC','Corinthiand','Grêmio','Atlético-MG','Vasco da Gama','Santos','EC Vitória','Juventude','Fortaleza','Sport Recife')

print('\nOs cinco primeiros colocados são:')
for c in Classificacao[0:5]:
    print(c)

print('\nOs quatro ultimos colocados são:')
for c in Classificacao[16:20]:
    print(c)

print('\nOs times em ordem alfabetica são:')
for c in sorted(Classificacao):
    print(c)

print(f'\nBahia está localizada na {Classificacao.index('Bahia')}ª posição:')



