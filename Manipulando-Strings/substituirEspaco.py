# 3. Faça uma função que recebe uma frase e substitui todas as ocorrências de espaço por “#”. Faça também uma função para realizar a entrada de dados. A saída de dados deve ser feita no programa principal.

def substituirEspaços (frase):

    for l in frase:
        novaFrase = frase.replace(' ', '#')

        return novaFrase

fraseDigitada = input('Digite uma frase: ')

print(substituirEspaços(fraseDigitada))



