''''num1 = int(input('Primerio numero? '))
num2 = int(input('Segundo numero? '))

resultado = num1 + num2

#print( 'a soma entre',num1,'e o numero',num2 ,'é igual a', resultado )

print ('a soma entre {} e {} , é igual a {}'.format(num1, num2, resultado))'''



''''
n = input('Digite algo: ')
print(n.isnumeric())'''


n1 = int(input('\033[1;31mDigite um numero:'))
n2 = int(input('Digite outro numero:\033[m'))

s = n1 + n2

print('\033[1;33mA soma entre {} mais {} é igual a {}'.format(n1, n2, s))