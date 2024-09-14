'''import math

valor = int(input('Digite o valor em metros: '))

c = valor * 100

m = valor * 1000

print('o numero digitado foi {} '
      'convertido em sentimetro {} '
      'convertido em milimetros {} '.format(valor, c , m))'''



valor = float(input('\033[1;34mDigite o valor em metros: '))


km = valor / 1000
hm = valor / 100
dam = valor / 10

dm = valor * 10
cm = valor * 100
mm = valor * 1000

print('km {} '.format(km))
print('hm {} '.format(hm))
print('dam {} '.format(dam))
print('dm {} '.format(dm))
print('cm {}' .format(cm))
print('mm {} '.format(mm))
