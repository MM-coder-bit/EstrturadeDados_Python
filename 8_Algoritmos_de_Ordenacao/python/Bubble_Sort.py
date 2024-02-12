# %%
import numpy as np

# %%
# Definição da função bubble_sort que ordena um vetor usando o algoritmo Bubble Sort.
def bubble_sort(vetor):
    # Obtém o tamanho do vetor.
    n = len(vetor)
    # Loop externo: percorre todo o vetor.
    for i in range(n):
        # Loop interno: percorre o vetor até a posição correta do elemento.
        for j in range(0, n - i - 1):
            # Verifica se o elemento atual é maior que o próximo elemento.
            if vetor[j] > vetor[j + 1]:
                # Troca os elementos se estiverem fora de ordem.
                temp = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = temp
    # Retorna o vetor ordenado.
    return vetor

# %%
# Cria um array NumPy para ordenar.
bubble_sort(np.array([15, 34, 8, 3]))

# %%
# Cria um array NumPy para ordenar.
bubble_sort(np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
