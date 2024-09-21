from datetime import date

ano = int(input('Qual ano voce nasceu: '))

atual = date.today().year

idade = atual - ano

print("Voce nasceu em {} tem anos {}".format(ano,idade))
if idade <= 9 :
    print('Mirin, sua idade {} anos'.format(idade))
elif idade <= 14 :
    print('infantil, sua idade {} anos'.format(idade))
elif idade <= 19 :
    print('Junior, sua idade {} anos'.format(idade))
elif idade <= 25 :
    print('Sênior, sua idade {} anos'.format(idade))
else:
    print('Master, sua idade {} anos'.format(idade))