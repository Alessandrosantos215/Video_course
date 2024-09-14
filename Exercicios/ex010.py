v = int(input('\033[1;33mQuanto voce tem na carteira?'))

d = 3.27

r = v / d

print('o valor que voce tem é R${} \n'
      'voce pode comprar {:.2f} Dolares \n'
      'valor do dolar hoje R${:.2f} '.format(v , r ,d))
