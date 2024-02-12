# %%
import numpy as np

# %%
# Definição da função selection_sort que ordena um vetor usando o algoritmo Selection Sort.
def selection_sort(vetor):
    # Obtém o tamanho do vetor.
    n = len(vetor)
    
    # Loop externo: percorre todo o vetor.
    for i in range(n):
        # Inicializa o índice do menor elemento como o índice atual.
        id_minimo = i

        # Loop interno: percorre o vetor a partir do próximo elemento.
        for j in range(i + 1, n):
            # Verifica se o elemento atual é menor que o menor elemento encontrado até agora.
            if vetor[id_minimo] > vetor[j]:
                # Atualiza o índice do menor elemento.
                id_minimo = j

        # Troca o elemento atual com o menor elemento encontrado.
        temp = vetor[i]
        vetor[i] = vetor[id_minimo]
        vetor[id_minimo] = temp

    # Retorna o vetor ordenado.
    return vetor


# %%
# Cria um array NumPy para ordenar.
selection_sort(np.array([15, 34, 8, 3]))

# %%
# Cria um array NumPy para ordenar.
selection_sort(np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))


