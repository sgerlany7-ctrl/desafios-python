lado1 = int(input('digite o primeiro lado: '))
lado2 = int(input('digite o segundo lado: '))
lado3 = int(input('digite o terceiro lado: '))
if lado1+ lado2 > lado3 and lado1+ lado3 > lado2 and lado2+ lado3 > lado1:
  if lado1 == lado2 and lado1 == lado3:
        print('se todos os lados forem iguais é EQUILATERO')

  elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('se um dos lados forem diferentes esse triangulo é ISÓCELES')
  elif lado1!= lado2 and lado1!= lado3 and lado2!= lado3:
         print('lados diferentes esse triangulo é ESCALENO')
else:
    print('As médidas informadas não forman um triangulo')