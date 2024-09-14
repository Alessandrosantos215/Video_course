l = int(input('\033[1;35mqual é a altura da parede? '))
a = int(input('Qual é a largura da parede? '))

area = a * l

t = area / 2

print('a largura da parede é {} \n'
      'a altura da parede é {} \n'
      'a area é {} \n'
      'voce precisa de {} litros de tinta para pintar a parede'.format(l , a, area ,t))