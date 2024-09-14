d = int(input('\033[1::41mQuantos dias alugado? '))
r = int(input('Quantos Km rodados? '))

v = d * 60

k = r * 0.15

t = v + k

print('o tocal a pagar é de R${} '.format(t))