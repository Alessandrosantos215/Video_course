import math

num = int(input('Digite um numero: '))

d = num * 2
t = num * 3
q = math.sqrt(num)

print('O numero digitado foi {} o dobro é {} o triplo é {} '
      'a raiz qudrada é {:.2f} '.format(num , d, t, q))
