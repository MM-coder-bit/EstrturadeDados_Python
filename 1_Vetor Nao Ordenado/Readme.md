# Vetor Não Ordenado

## Descrição

A classe `VetorNaoOrdenado` representa uma estrutura de dados de vetor não ordenado em Python. Um vetor não ordenado é uma coleção de elementos que não segue uma ordem específica, e os elementos são armazenados em posições contíguas de memória.

## Funcionalidades

### Inicialização

Ao criar um objeto da classe, é necessário fornecer a capacidade inicial do vetor.

```python
vetor = VetorNaoOrdenado(capacidade)
```

### Inserção

A inserção de um valor no vetor é realizada pela função `insere`. Caso a capacidade máxima seja atingida, uma mensagem será exibida.

```python
vetor.insere(valor)
```

### Impressão

A função `imprime` exibe todos os elementos presentes no vetor.

```python
vetor.imprime()
```

### Pesquisa

A função `pesquisar` verifica se um determinado valor está presente no vetor. Retorna o índice do valor se encontrado, ou -1 se não estiver presente.

```python
indice = vetor.pesquisar(valor)
```

### Exclusão

A função `excluir` remove um valor específico do vetor. Se o valor não for encontrado, retorna -1.

```python
vetor.excluir(valor)
```

## Complexidade de Tempo

- Inserção: O(1)
- Pesquisa: O(n)
- Exclusão: O(n)

## Exemplo de Uso

```python
# Criar um vetor com capacidade 5
vetor = VetorNaoOrdenado(5)

# Inserir valores no vetor
vetor.insere(10)
vetor.insere(20)
vetor.insere(30)

# Imprimir o vetor
vetor.imprime()  # Output: 0 - 10, 1 - 20, 2 - 30

# Pesquisar um valor no vetor
indice = vetor.pesquisar(20)
print(indice)  # Output: 1

# Excluir um valor do vetor
vetor.excluir(20)

# Imprimir o vetor após exclusão
vetor.imprime()  # Output: 0 - 10, 1 - 30
```

Este README fornece uma visão geral simples da estrutura de dados do vetor não ordenado e demonstra seu uso básico.