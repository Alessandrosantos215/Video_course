somaidade = 0
médiaidade = 0
maioridade = 0
nomevelho= ''
totmulher20 = 0
for p in range(1, 5 ):
    print('----{}ºPESSOAS -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p== 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridade, nomevelho))
print('Ao todo são {}mulheres com menos de 20 anos'.format(totmulher20))