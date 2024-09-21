n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2

print('\033[1;34mMedia é igual a {}'.format(m))

if  7 > m >= 5 :
    print('recuperação sua media foi {}'.format(m))
elif m < 5:
    print('Reprovado sua media foi {}'.format(m))
elif m >=7 :
    print('Aprovado sua media foi {}'.format(m))

