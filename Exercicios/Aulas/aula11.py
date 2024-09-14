'''\033[0:33:44m]
\033 sempre começa assim

0 style
33 text
44m back

------------********-------
style

0 none
1 bold
4 underline
7 negative

----------**********------------
text

30 branco
31 vermenlho
32 verde
33 amarelo
34 azul
35 magenta
36 siano
37 cinza

-----------***********----------
back

40 branco
41 vermenlho
42 verde
43 amarelo
44 azul
45 magenta
46 siano
47 cinza


----------*********-----------

\033[0:30:41m]
\033[0:33:44m]
\033[1:35:43m]
\033[30:42m]
\033[m]
\033[7:30m]

----------***********------------
print('\033[4;30;45mOlá, Mundo!\033[m')

---------**********------------
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

---------***********----------
nome = 'Alessandro'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))


--------************---------------'''

nome = ('Alessandro')
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m'
         'pretoebranco':'\033[7;30m'

print('Olá muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))