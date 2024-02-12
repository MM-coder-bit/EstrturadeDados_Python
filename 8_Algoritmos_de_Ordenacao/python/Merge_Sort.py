# %%
import numpy as np

# %%
# Definição da função merge_sort que ordena um vetor usando o algoritmo Merge Sort.
def merge_sort(vetor):
    # Verifica se o vetor tem mais de um elemento.
    if len(vetor) > 1:
        # Divide o vetor ao meio.
        divisao = len(vetor) // 2
        esquerda = vetor[:divisao].copy()
        direita = vetor[divisao:].copy()

        # Chama recursivamente merge_sort para as sub-listas esquerda e direita.
        merge_sort(esquerda)
        merge_sort(direita)

        # Inicializa índices para percorrer as sub-listas e o vetor original.
        i = j = k = 0

        # Combina as sub-listas ordenadas de volta ao vetor original.
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                vetor[k] = esquerda[i]
                i += 1
            else:
                vetor[k] = direita[j]
                j += 1
            k += 1

        # Adiciona os elementos restantes da sub-lista esquerda, se houver.
        while i < len(esquerda):
            vetor[k] = esquerda[i]
            i += 1
            k += 1

        # Adiciona os elementos restantes da sub-lista direita, se houver.
        while j < len(direita):
            vetor[k] = direita[j]
            j += 1
            k += 1

    # Retorna o vetor ordenado.
    return vetor


# %%
# Cria um array NumPy para ordenar.
merge_sort(np.array([15, 34, 8, 3]))

# %%
# Cria um array NumPy para ordenar.
merge_sort(np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))


