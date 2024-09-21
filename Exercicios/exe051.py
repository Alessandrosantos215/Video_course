primeiro = int(input('Digite o primeiro termo: '))
razão = int(input( 'Digite o segundo termo: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{} '.format(c), end='-> ')
print('ACABOU')
