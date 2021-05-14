# 4. Escreva um programa que leia o nome de uma pessoa e verifique se ela tem “Silva” em seu nome.

nome = input('Escreva seu nome completo: ')
nomeMinusculo = nome.lower()


if 'silva' in nomeMinusculo:
    print('Possui o sobrenome Silva.')
else:
    print('Não possui o sobrenome Silva')

