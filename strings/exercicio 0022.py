

frase=str(input('qual o seu nome? ')).strip()
print('analizando o seu nome ....')
print('seu nome em maiusculo é:',frase.upper())
print('seu nome em menusculo é:',frase.lower())
print('seu nome tem {} letras'.format(len(frase)-frase.count(' ')))
print('seu primeiro nome tem {} letras'.format(frase.find(' ')))






