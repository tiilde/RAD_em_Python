# 2. Escreva um programa que leia o número de 0 a 9999 e mostre na tela todos os números separados.
# Ex. 1974 => unidade 4, dezena 7, centena 9, milhar 1 


num = int(input('Digite um número de 0 a 9999: ' ))


if num >= 0 and num <= 9999:
    if num <= 9:

        print(f'{num} => unidade {num}')

    if num >= 10 and num <= 99:

        print(f'{num} => dezena {str(num)[0]}, unidade {str(num)[1]}')

    if num >= 100 and num <= 999:

        print(f'{num} => centena {str(num)[0]}, dezena {str(num)[1]}, unidade {str(num)[2]}')

    if num >= 1000 and num <= 9999:

        print(f'{num} => milhar {str(num)[0]}, centena {str(num)[1]}, dezena {str(num)[2]}, unidade {str(num)[3]}')
    
else: 
    print('Número acima do valor aceito')

