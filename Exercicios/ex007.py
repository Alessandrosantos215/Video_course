nota1 = float(input('\033[1;35mdigite primeira nota: '))
nota2 = float(input('Digite segunda nota: '))

s = nota1 + nota2

m = s / 2

print('a primera nota foi {} '
      'a segunda nota foi {} '
      'a soma é igual a {} '
      'a média é {}'.format(nota1, nota2 ,s , m))

if m >= 5:
    print('aprovado')
else:
    print('reprovado')