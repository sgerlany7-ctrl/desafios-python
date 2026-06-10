casa = float(input('Qual o valor da casa? '))
salario = float(input('qual valor do salario? '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'para pagar uma casa de R$ {casa:.2f} em {anos} anos')
print(f'a prestação será de R$ {prestacao:.2f}')
if prestacao <= minimo:
    print('seu emprestimo foi aprovado')
else:
    print('seu emprestimo foi negado')
