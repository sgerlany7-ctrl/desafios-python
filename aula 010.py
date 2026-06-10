nome = str(input('qual é o seu nome? '))
if nome == 'gerlany':
    print ('que nome bonito!')
    #qundo tem o else é composta, quando não tem é simpes
else:
    print('não gosto do seu nome!')
print('bom dia,{}!'.format(nome))

n1 = float(input('digite a primeira nota '))
n2 = float(input('digite a segunda nota '))
m =(n1+n2)/2
print ('a sua media foi{:.1f}'.format(m))
if m>=6.0:
 print('a sua nota foi boa! PARABÉNS!')
else:
    print('a sua nota foi ruim!ESTUDE MAIS!')