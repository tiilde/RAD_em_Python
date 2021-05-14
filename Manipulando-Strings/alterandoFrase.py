# 1. Escreva uma função que recebe uma frase e uma palavra antiga e uma palavra nova. A função deve retornar uma string contendo a frase original, mas com a última ocorrência da palavra antiga substituída pela palavra nova. A entrada e saída de dados deve ser feita no programa principal. (????)

# Exemplo:
# Frase: “Quem parte e reparte fica com a maior parte”
# Palavra antiga: “parte”
# Palavra nova: “parcela”
# Resultado a ser impresso no programa principal: “Quem parte e reparte fica com a maior parcela”


def alterandoFrase (frase, palavraAntiga, palavraNova):

    novaFrase = frase.replace(palavraAntiga, palavraNova)
    return novaFrase



frase = input('Digite uma frase: ')
palavraAntiga = input('Qual a palavra que você deseja trocar? ')
palavraNova = input('Por qual palavra você deseja substituir a palavra antiga? ')

print(f'Frase original: {frase}')
print(alterandoFrase(frase, palavraAntiga,palavraNova))

