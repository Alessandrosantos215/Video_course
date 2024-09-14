p = int(input('\033[1;34mqual é o preço do produto?'))

desconto = p * 0.05

d = p - desconto

print('o valor do produto é R${}\n'
      'com o desconto de 5% fica R${}'.format(p , d ))