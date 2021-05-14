# 1. Escreva um programa que leia o nome completo de uma pessoa e mostre: 

# a)	o nome com todas as letras em maiúscula
# b)	o nome com todas as letras em minúsculas
# c)	quantas letras ao todo (desconsiderar os espaços em branco)
# d)	quantas letras tem o primeiro nome



nome = input('Digite seu nome completo: ')
nomeSemEspaço = nome.replace(" ", "")
listaNome = nome.split()

print('Dados sobre o nome\n'.upper())
# a
print('Nome em letras maíúsculas: ', nome.upper())
#b
print('Nome em letras minúsculas: ', nome.lower())
# c
print('Total de letras no nome: ', len(nomeSemEspaço))
# d
print('Total de letras no primeiro nome: ', len(listaNome[0]))
