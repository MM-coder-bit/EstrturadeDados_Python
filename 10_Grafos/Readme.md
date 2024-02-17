
# Grafos

Um grafo é uma estrutura de dados que representa relações entre elementos. Consiste em um conjunto de vértices (ou nós) e um conjunto de arestas (ou arcos) que conectam pares de vértices. Os grafos podem ser direcionados, onde as arestas têm uma direção específica, ou não direcionados.

## Conceitos Básicos

- **Vértices (ou Nós):** São os elementos individuais do grafo.
- **Arestas (ou Arcos):** São as conexões entre pares de vértices.
- **Grafo Não Direcionado:** As arestas não têm direção, ou seja, a relação é bidirecional.
- **Grafo Direcionado:** As arestas têm direção, indicando uma relação unidirecional.
- **Grafo Ponderado:** As arestas têm um peso associado, representando algum valor numérico.
- **Grafo Conectado:** Existe um caminho entre cada par de vértices no grafo.
- **Grafo Não Conectado:** Pode haver vértices não alcançáveis por outros vértices no grafo.

## Representações

### Lista de Adjacência

Cada vértice tem uma lista de seus vértices adjacentes. É uma representação eficiente para grafos esparsos.

Exemplo:
```python
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
    'G': ['C']
}
```

### Matriz de Adjacência

Uma matriz onde cada elemento `A[i][j]` representa se há uma aresta entre os vértices `i` e `j`. Pode incluir pesos das arestas.

Exemplo:
```
    A B C D E F G
A | 0 1 1 0 0 0 0
B | 1 0 0 1 1 0 0
C | 1 0 0 0 0 1 1
D | 0 1 0 0 0 0 0
E | 0 1 0 0 0 1 0
F | 0 0 1 0 1 0 0
G | 0 0 1 0 0 0 0
```

## Algoritmos e Operações

### Busca em Profundidade

Um algoritmo que explora o grafo o mais longe possível ao longo de cada ramo antes de retroceder.

### Busca em Largura

Um algoritmo que explora todos os vértices de um grafo em "camadas", visitando todos os vizinhos de um vértice antes de avançar.

### Busca Gulosa

Uma estratégia de busca que seleciona o caminho mais promissor até o momento, sem considerar o custo total.

### Busca A* (A Estrela)

Uma estratégia de busca informada que avalia os vértices considerando tanto o custo até o momento quanto uma estimativa do custo restante.

### Dijkstra

Um algoritmo para encontrar o caminho mais curto entre dois vértices em um grafo ponderado, sem arestas de peso negativo.

### Referências

- [Wikipedia - Grafo](https://pt.wikipedia.org/wiki/Grafo)
- [GeeksforGeeks - Graph Data Structure And Algorithms](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/)
- Livro: "Introduction to Algorithms" - Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein.

Este README oferece uma introdução abrangente aos conceitos básicos dos grafos, suas representações e alguns algoritmos fundamentais.