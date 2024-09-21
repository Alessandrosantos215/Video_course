from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2 )
print('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('\033[1;33mJO\033[m')
sleep(1)
print('\033[1;34mKEN\033[m')
sleep(1)
print('\033[1;32mPO!!!\033[m')
sleep(1)
print('\033[1;35m-= ' * 15)

print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-= '* 15 )
print('\033[m')

if computador == 0:
    if jogador == 0:
        print('\033[1;34mEMPATE \033[m')
    elif jogador == 1:
        print('\033[1;32mJOGADOR VENCE \033[m')
    elif jogador == 2:
        print('\033[1;31mCOMPUTADOR VENCE \033[m')
    else:
        print('JOGADA INVALIDA')

elif computador == 1:
    if jogador == 0:
        print('\033[1;31mCOMPUTADOR VENCE \033[m')
    elif jogador == 1:
        print('\033[1;34mEMPATE \033[m')
    elif jogador == 2:
        print('\033[1;32mJOGADOR VENCE \033[m')
    else:
        print('JOGADA INVALIDA')

elif computador == 2:
    if jogador == 0 :
        print('\033[1;32mJOGADOR VENCE \033[m')
    elif jogador == 1:
        print('\033[1;31mCOMPUTADOR VENCE \033[m')
    elif jogador == 2:
        print('\033[1;34mEMPATE \033[m')
    else:
        print('JOGADA INVALIDA')
else:
    print('JOGADA INVALIDA')