from random import choice

n1 = input('digite o primeiro nome: ')
n2 = input('digite o primeiro nome: ')
n3 = input('digite o primeiro nome: ')
n4 = input('digite o primeiro nome: ')

Lista = [n1 , n2 , n3 , n4]

s = choice(Lista)



print('O aluno escolhido foi {}' .format(s))


