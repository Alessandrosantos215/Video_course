import math

num = int(input('Digite um numero: '))

numrad = math.radians(num)

co = math.cos(numrad)
sen = math.sin(numrad)
tan = math.tan(numrad)

'''sen= math.sin.(mathradians(num))
   co math.cos(math.radians(num))
   tan = math.tan(math.radians(num))'''

print('O numero digitado foi {:.2f}\n'
      'o seno é {:.2f} \n'
      'o cosseno é {:.2f} \n'
      'a tangente é {:.2f}'.format(num , sen , co , tan))
