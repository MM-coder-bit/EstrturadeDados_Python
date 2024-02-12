# %%
import numpy as np

# %%
# Função particao que retorna a posição do pivo após particionar o vetor.
def particao(vetor, inicio, final):
    # Escolhe o pivo como o último elemento do vetor.
    pivo = vetor[final]
    i = inicio - 1

    # Loop para percorrer o vetor e particionar os elementos menores e maiores que o pivo.
    for j in range(inicio, final):
        if vetor[j] <= pivo:
            i += 1
            # Troca os elementos para movê-los para a parte correta do vetor.
            vetor[i], vetor[j] = vetor[j], vetor[i]

    # Troca o pivo para a posição correta.
    vetor[i + 1], vetor[final] = vetor[final], vetor[i + 1]

    # Retorna a posição do pivo após a partição.
    return i + 1

# Função quick_sort que ordena um vetor usando o algoritmo Quick Sort.
def quick_sort(vetor, inicio, final):
    if inicio < final:
        # Obtém a posição do pivo após a partição.
        posicao = particao(vetor, inicio, final)

        # Chama recursivamente quick_sort para a parte esquerda do vetor.
        quick_sort(vetor, inicio, posicao - 1)

        # Chama recursivamente quick_sort para a parte direita do vetor.
        quick_sort(vetor, posicao + 1, final)

    # Retorna o vetor ordenado.
    return vetor


# %%
# Cria um array NumPy para ordenar.
vetor = np.array([15, 34, 8, 3])

# Chama a função quick_sort para ordenar o array.
quick_sort(vetor, 0, len(vetor) - 1)

# %%
# Cria um array NumPy para ordenar.
vetor = np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

# Chama a função quick_sort para ordenar o array.
quick_sort(vetor, 0, len(vetor) - 1)


