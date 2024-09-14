num = int(input('Digite um nuemro inteiro: '))
print('''Escolha uma das bases para a conveção
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} converter para BINARIO é igual a {}'.format(num, bin(num)))
elif opção ==2:
    print('{} converter para OCTAL é igual a {}'.format(num, oct(num)))
elif opção ==3:
    print('{} converter para HEXADECIMAL é igual a {}'.format(num, hex(num)))
else:
    print('Opção invalida. Tente novamente')

