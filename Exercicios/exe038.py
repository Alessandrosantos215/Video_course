v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
if v1 > v2:
    print('\033[1;34mO primeiro valor é maior')
elif v1 < v2:
    print('\033[1;35mO segundo valor é maior')
elif v1 == v2:
    print('\033[1;36mOs dois valores são iguais')