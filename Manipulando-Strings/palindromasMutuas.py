# 4. Faça um programa que decida se duas strings lidas do teclado são palíndromas mútuas, ou seja, se uma é igual à outra quando lida de traz para frente.
# Exemplo: amor e roma.

# as letras tem que ser as mesmas
# quantidade de letras

palavra1 = input('Digite uma palavra: ')
palavra2 = input('Digite uma outra palavra: ')


if palavra1 == palavra2[:: -1]:
    print('São palavras palídromas mútuas.')
else:
    print('Não são palavras palíndromas.')
   

