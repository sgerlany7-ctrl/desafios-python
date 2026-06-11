#nun=int(input('digite um numero:' ))
#n= str(nun)
#print('analizando o numero {}'.format(nun))
#print('unidade {}'.format(n[3]))
#print('dezena {}'.format(n[2]))
#print('centena {}'.format(n[1]))
#print('milhar {}'.format(n[0]))
nun=int(input('digite um numero: '))
u=nun//1%10
d=nun//10%10
c=nun//100%10
m=nun//1000%10
print('analizando o numero {} ....'.format(nun))
print('unidade:{} '.format(u))
print('dezena:{} '.format(d))
print('centena:{} '.format(c))
print('milhar: {} '.format(m))




