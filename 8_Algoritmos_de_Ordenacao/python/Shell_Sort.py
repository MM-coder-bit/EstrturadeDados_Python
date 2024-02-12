# %%
import numpy as np

# %%
# Definição da função shell_sort que ordena um vetor usando o algoritmo Shell Sort.
def shell_sort(vetor):
    # Define o intervalo inicial como metade do tamanho do vetor.
    intervalo = len(vetor) // 2

    # Loop externo: continua enquanto o intervalo é maior que zero.
    while intervalo > 0:
        # Loop interno: percorre o vetor a partir do intervalo até o final.
        for i in range(intervalo, len(vetor)):
            # Armazena temporariamente o elemento atual.
            temp = vetor[i]
            j = i

            # Loop interno: move os elementos maiores que o temporário para a direita.
            while j >= intervalo and vetor[j - intervalo] > temp:
                vetor[j] = vetor[j - intervalo]
                j -= intervalo

            # Coloca o elemento temporário na posição correta.
            vetor[j] = temp

        # Reduz o intervalo pela metade.
        intervalo //= 2

    # Retorna o vetor ordenado.
    return vetor


# %%
# Cria um array NumPy para ordenar.
shell_sort(np.array([15, 34, 8, 3]))

# %%
# Cria um array NumPy para ordenar.
shell_sort(np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))


