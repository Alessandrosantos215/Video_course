nome = str(input('Digite o nome completo: ')).strip()

palavra = nome.split()

primeira_palavra = palavra[0]

numero_de_letras = len(primeira_palavra)


print('todas maiusculas:',nome.upper())
print('='*22)
print('Todas minsculas:',nome.lower())
print('='*22)
print('contagem sem espaço:',len(nome) - nome .count(' '))
print('='*22)
print('a primeira palavra é {} e ela tem {} de letras '.format(primeira_palavra , numero_de_letras))


