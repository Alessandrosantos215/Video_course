from random import   shuffle

n1 = input('digite o nome do aluno: ')
n2 = input('digite o nome do aluno: ')
n3 = input('digite o nome do aluno: ')
n4 = input('digite o nome do aluno: ')

Lista = [ n1 , n2 , n3 , n4]

s = shuffle(Lista)

print('a ordem das apresentações são {}'.format(Lista))