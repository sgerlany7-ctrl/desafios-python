ano = int(input('qual ano de nascimento? '))
idade = 2026 - ano
if idade <=9:
    print('o atleta esta na categoria MIRIN')
elif idade <=14:
    print(f'o atleta tem {idade} anos é está na categoria INFANTIL')
elif idade <=19:
    print(f'o atleta tem {idade} anos é está na categoria JUNIOR')
elif idade <=25:
    print(f'o atleta tem {idade} anos é está na categoria SENIOR')
else:
    print(f'o atleta tem {idade} anos é está na categoria MASTER')