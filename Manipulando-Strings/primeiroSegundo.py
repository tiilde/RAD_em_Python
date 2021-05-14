# 6. Escreva um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e último nome dessa pessoa. Ex: Ana Maria Soares => primeiro: Ana, último: Soares.


nome = input('Dgite seu nome completo: ')
nomeLista = nome.split()

print(f'Primeiro nome: {nomeLista[0]}')
print(f'Último nome: {nomeLista[-1]}')
