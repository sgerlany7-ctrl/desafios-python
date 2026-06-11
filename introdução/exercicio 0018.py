import math
val=int(input('qual o angulo ?: '))
angulos_radianos=math.radians(val)
seno=math.sin(math.radians(val))
cons=math.cos(math.radians(val))
tan=math.tan(math.radians(val))
print('o angulo {} em radiano é {:.2f} \n o valor em seno é {:.2f} \n o valor em cosseno é {:.2f} \n é o valor em tangeno é {:.2f}'.format(val,angulos_radianos,seno,cons,tan))

#ver como fazz +- certo