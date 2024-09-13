s = int(input('Digite seu salario:'))

a = s * 0.15

r = s + a

print('o salario é R${}  \b'
      'com o aumento de 15% fica R${:.0f}'.format(s ,r))