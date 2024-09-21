from time import sleep
n = int(input('Digite um numero: '))
sleep(1)
print(' contage de 1 até {} apenas numeros pares'.format(n))

for c in range(0, n+1, 2 ):
    print('\033[1;35m')
    print(c, )