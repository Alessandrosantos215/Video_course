
frase = 'Curso em Video Python'
print(frase[9:13])
print(frase.upper('O')) conta quantas vezes tem O maiusculo na fraze que ficou com tudo maiusculo
print(len(frase)) vai contar quanto tem de frase contando espaços juntos
print(len(frase.strip())) vai remover os espaços
frase = frase.replace ('Python','Android') vai substituir

frase ='Curso em Video Python'
dividido = frase.split()
print(dividido[0])vai criar listas com as palavras e vai printar a primeira

dividido = frase.split()
print(dividido [2] [3]) vai pegar a segunda lista e mostrar a 3 letra



print(frase.find ('video')) vai mostras a posição da palavra

print(fraase. lower().find('video')) vai encontrar a palavra em minusculo



'''frase [9]
frase [9:13] exclui o ultimo
frase [9:21:2]pular de dois em dois
frase [:5]  do 0 até o 4
frase [15:] do 15 até o final
frase [9::13] pula três em três

len (frase) vai mostrar quanto tem de espaço a frase
frase.count('o') vai contar quantos 'o'tem
frase.count('o',0,13)contas quantos 'o' no intervalo
frase.find('deo') vai procurar na frase se não encontrar vai aparecer -1
'Curso 'in frase - verdadeir ou falso
frase.replace('Python','Androide') vai procurar e substituir
frase.upper() faz tudo ficar maisculo
frase.lower() fa ficar tudo minusculo
frase.captalize() a primeira letra maiuscula
frase.title() todas as primeiras letras maiuscula

frase.strip() vai eliminar espços no começo e no fim
frase.rstrip() remove o do lado direita
frase.lstrip() remove do lado esquerdo

frase.split() vai refazer cada indce,gera uma lista em cada espaço de caracteres
'-'.join(frase) vai acrecentar'-'nos espaços vazios

'''