
algo = input('\033[1;31mDigite algo: ')

print ('O tipo primitivo',type(algo))
print ('É numero ?{}'.format(algo.isnumeric()))
print ('É letra ?{}'.format(algo.isalpha()))
print ('É alfa numerico ?{}'.format(algo.isalnum()))
print ('É apenas em letra maiuscula ?{}'.format(algo.isupper()))
print ('Esta em maiuscula ?{}'.format(algo.isupper()))
print ('Esta em minuscula ?{}'.format(algo.islower()))
print ('Esta captalizada ?{}'.format(algo.istitle()))