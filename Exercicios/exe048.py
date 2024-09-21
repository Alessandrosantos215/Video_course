'''from time import sleep
n = int(input('Digite um numero: '))
sleep(1)
print('Todos os numeros multiplos de 3 do numero {}'.format(n))
for c in range(0, n+1 ):
    print(c)
    sleep(0.1)
print('\033[1;33mCarregando soma...\033[m')
sleep(1)
s = (c + c) / 3
print('\033[1;35mValor total :{:.2f}'.format(s))'''

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A doma de todos os {} valores solicitados é {}'.format(cont, soma))

