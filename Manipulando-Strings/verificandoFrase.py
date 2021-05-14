# 5. Escreva um programa que leia uma frase e mostre:

# a)	quantas vezes aparece a letra “a”.
# b)	em que posição ela aparece a primeira vez.
# c)	em que posição ela aparece a última vez.


frase = input('Escreva uma frase: ')
fraseAnalisada = frase.lower()


print(frase)

print('Dados sobre essa frase:'.upper())
# a
print(f'A letra "a" aparece {fraseAnalisada.count("a")} vezes nessa frase')
# b
print(f'A letra "a" aparece pela primeira vez na posição [{fraseAnalisada.find("a")}]')
# c
print(f'A letra "a" aparece pela última vez, na posição [{fraseAnalisada.rfind("a")}]')

