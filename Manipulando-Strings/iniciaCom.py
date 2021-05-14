# 3. Escreva um programa que leia o nome de uma cidade e verifique se a mesma inicia ou não com o nome “Fort”.



nCidade = input('Digite o nome de uma cidade: ')
cidade = nCidade.startswith('Fort')

print(cidade)


# Caso tenha que considerar fort em minusculo, então seria essa a solução abaixo:

# nCidade = input('Digite o nome de uma cidade: ')
# nLetraMaiuscula = nCidade.capitalize()
# comecaCom = nLetraMaiuscula.startswith('Fort')

# print(comecaCom)





