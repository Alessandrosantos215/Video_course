from random import randint
from time import sleep
computador = randint(0, 5)# Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? ')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você consguiu vencer!')
else:
    print('GANHEI! Eu pensei no numero {} e não é {}!'.format(computador, jogador))