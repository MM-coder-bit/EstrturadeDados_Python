# %%
import numpy as np

# %%
# Definição da função insertion_sort que ordena um vetor usando o algoritmo Insertion Sort.
def insertion_sort(vetor):
    # Obtém o tamanho do vetor.
    n = len(vetor)

    # Loop externo: percorre o vetor começando do segundo elemento.
    for i in range(1, n):
        # Armazena o elemento atual que será movido para a posição correta.
        marcado = vetor[i]

        # Inicializa o índice j para comparar com o elemento marcado.
        j = i - 1

        # Loop interno: move os elementos maiores que o marcado para a direita.
        while j >= 0 and marcado < vetor[j]:
            vetor[j + 1] = vetor[j]
            j -= 1

        # Coloca o elemento marcado na posição correta.
        vetor[j + 1] = marcado

    # Retorna o vetor ordenado.
    return vetor


# %%
# Cria um array NumPy para ordenar.
insertion_sort(np.array([15, 34, 8, 3]))

# %%
# Cria um array NumPy para ordenar.
insertion_sort(np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))


