nota1 = float(input('qual a primeira nota do aluno? '))
nota2 = float(input('qual a segunda nota do aluno? '))
media = (nota1 + nota2) / 2
if media < 5:
    print(f' você foi REPROVADO, sua nota foi {media}')
elif media <= 7:
    print(f'RECUPERAÇÃO! sua nota foi {media}')
else:
    print(f'APROVADO! sua nota foi {media}')
