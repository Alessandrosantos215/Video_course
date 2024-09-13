'''num = int(input('Digite um numero: '))
n= str (num)
print('Analisando o número {}'.format(num))
print('Unidade {}'.format(n[3]))
print('Dezena {}'.format(n[2]))
print('centena {}'.format(n[1]))
print('Milhar {}'.format(n[0])'''


num = int(input('Digite um número : '))

# Extrai cada dígito do número
unidade = num % 10
dezena = (num // 10) % 10
centena = (num // 100) % 10
milhar = (num // 1000) % 10

# Exibe os resultados
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')