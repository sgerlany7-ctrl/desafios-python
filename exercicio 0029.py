velocidade =float(input('digite a velocidade '))
if velocidade > 80:
    multa = (velocidade -80) * 7
    print('você foi multado!')
    print(f'A multa custa r${multa:.2f}')
print ('Dirija com cuidado!')
