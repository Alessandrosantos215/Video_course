numero = int(input('Digite um numero qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O numero {} é par'.format(numero))
else:
    print('O numero {} é IMPAR'.format(numero))