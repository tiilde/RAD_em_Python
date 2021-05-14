# 2. Faça uma função que recebe uma frase e retorna o número de palavras que a frase contém. Considere que a palavra pode começar e/ou terminar por espaços. A entrada e saída de dados deve ser feita no programa principal.

def numeroPalavras (frase):
    
    listaDePalavras = frase.split()
    return f'Essa frase contém {len(listaDePalavras)} palavras.'


fraseEntrada = input('Escreva uma frase: ')
print(numeroPalavras(fraseEntrada))