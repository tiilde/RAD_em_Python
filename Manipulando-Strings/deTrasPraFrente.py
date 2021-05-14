# 5. Faça um programa que leia o nome do usuário e mostre o nome de trás para frente, utilizando somente letras maiúsculas.

nomeUsuario = input('Digite seu nome: ')

nomeInvertido = nomeUsuario[:: -1].upper()
print(nomeInvertido)