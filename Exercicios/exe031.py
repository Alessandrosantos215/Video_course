distancia = float(input('Qual é a distancia da sua viagem? '))
print('Você esta prestes a começar uma viagem de {}Km'.format(distancia))
if distancia <= 200:
     preço = distancia * 0.50
else:
     preço = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))


'''distancia = float(input('Qual é a distancia da sua viagem? '))
print('Você esta prestes a começar uma viagem de {}Km'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 10000.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))'''