# 6. Faça um programa que leia o nome do usuário e o imprima na vertical, em forma de escada, usando apenas letras maiúsculas.

# Exemplo:
# Nome = Vanessa
# Resultado gerado pelo programa: 
# V
# VA
# VAN
# VANE
# VANES
# VANESS
# VANESS A


nomeConcatenado = ''
nome = input('Digite seu nome: ')

for l in range(0, len(nome)):
    nomeConcatenado = nomeConcatenado + nome[l]
    print(nomeConcatenado.upper())


