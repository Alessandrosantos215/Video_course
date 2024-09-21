'''laço c no intervalo(1, 10)
    passo
pega

--------*********---------
for c in range(1, 10):
        passo
pega


-------********----------
for ce in range (0, 3):
    passo
    pula
passo
pega

---------*********------
for c in range(0, 3):
    se moeda:
        pega
    passo
    pula
passo
pega

----------************----
for c in range (0,6):
    print(c)
print('Fim')

------*********---------

for c in range (0,60, 2):
    print(c)
print('Fim')

--------******--------
for c in range (6, 0 ,-1):
    print(c)
print('Fim')

--------*******--------
n = int(input('Digite um numero: '))
for c in range (0, n+1):
    print(c)

-----------********------
i = int(input('inicio: '))
f = int(input('fim: '))
p = int(input('passo: '))
for c in range(i , f+1 , p ):
    print(c)

---------**********-------
for c in range(0 , 3):
    n = input('Digite um valor: ')
print('FIM')

    '''
s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n
print('O somatorio de todos os valores foi \033[1;35m{}'.format(s))


