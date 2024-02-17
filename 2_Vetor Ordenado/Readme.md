# Vetor Ordenado e Vetor Ordenado com Busca Binária

## Vetor Ordenado

### Descrição

A classe `VetorOrdenado` representa um array ordenado com capacidade fixa em Python. Nesse tipo de estrutura de dados, os elementos são armazenados de maneira ordenada, facilitando operações como busca binária.

### Funcionalidades

- **Inicialização:** Ao criar um objeto da classe, é necessário fornecer a capacidade inicial do vetor.

```python
vetor = VetorOrdenado(capacidade)
```

- **Inserção:** A inserção de um valor no vetor é realizada pela função `insere`. Caso a capacidade máxima seja atingida, uma mensagem será exibida.

```python
vetor.insere(valor)
```

- **Impressão:** A função `imprime` exibe todos os elementos presentes no vetor.

```python
vetor.imprime()
```

- **Pesquisa Linear:** A função `pesquisa_linear` realiza uma busca linear por um valor no vetor.

```python
indice = vetor.pesquisa_linear(valor)
```

- **Exclusão:** A função `excluir` remove um valor específico do vetor.

```python
vetor.excluir(valor)
```

### Complexidade de Tempo

- Inserção: O(n)
- Pesquisa Linear: O(n)
- Exclusão: O(n)

## Vetor Ordenado com Busca Binária

### Descrição

A classe `VetorOrdenado` com busca binária representa um array ordenado que utiliza o algoritmo de busca binária para melhorar a eficiência da pesquisa.

### Funcionalidades

As funcionalidades são semelhantes às do Vetor Ordenado, mas a pesquisa é realizada de maneira mais eficiente utilizando o algoritmo de busca binária.

- **Pesquisa Binária:** A função `pesquisa_binaria` realiza uma busca binária por um valor no vetor.

```python
indice = vetor.pesquisa_binaria(valor)
```

### Complexidade de Tempo

- Inserção: O(n)
- Pesquisa Binária: O(log n)
- Exclusão: O(n)

## Exemplo de Uso

```python
# Criar um vetor ordenado com capacidade 5
vetor_ordenado = VetorOrdenado(5)

# Inserir valores no vetor
vetor_ordenado.insere(30)
vetor_ordenado.insere(10)
vetor_ordenado.insere(20)

# Imprimir o vetor ordenado
vetor_ordenado.imprime()  # Output: 0 - 10, 1 - 20, 2 - 30

# Pesquisar um valor no vetor utilizando busca binária
indice = vetor_ordenado.pesquisa_binaria(20)
print(indice)  # Output: 1

# Excluir um valor do vetor
vetor_ordenado.excluir(20)

# Imprimir o vetor após exclusão
vetor_ordenado.imprime()  # Output: 0 - 10, 1 - 30
```

Este README fornece uma visão geral simples das classes `VetorOrdenado` e `VetorOrdenado` com busca binária e demonstra seu uso básico.