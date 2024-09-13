frase = str(input('Digite uma frase: ')).upper().strip()
print('A lestra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primerira letra A aparece na posição {}'.format(frase.find('A')+1))
print('A ultimaletra Aapareceu na posição {}'.format(frase.rfind('A')+1))