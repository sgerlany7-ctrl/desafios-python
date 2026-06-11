ano = int(input('digite o ano de nascimento: '))
idade = 2025 - ano
print(f'quantos anos tem? {idade} ')
if idade < 18:
    faltam = 18 - idade
    print(f'ainda vai se alistar no exercito brasileiro  faltam {faltam} anos ')
elif idade == 18:
    print(f'é hora de se alistar ')
else:
    passou = idade - 18
    print(f'não podera se alistar passou {passou} anos do prazo ')