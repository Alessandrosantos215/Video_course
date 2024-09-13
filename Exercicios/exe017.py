import math

co = int(input('Digite cateto oposto:'))
ca = int(input('Digitecateto adjacente:'))

hipo = math.hypot(co, ca)

print('cateto oposto é {} cateto adjacente {}\n'
      'cumprumento da hipotenusa {:.2f}'.format(co , ca , hipo))
