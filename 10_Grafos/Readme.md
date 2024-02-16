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

### Caminhos

- **Caminho:** Sequência de vértices onde cada vértice é adjacente ao próximo.
- **Caminho Mínimo:** Caminho com o menor custo ou peso entre dois vértices.
- **Ciclo:** Caminho fechado onde o vértice inicial é igual ao vértice final.

### Árvores Geradoras

Uma árvore geradora de um grafo conectado é uma subestrutura que inclui todos os vértices do grafo, mas sem ciclos.

### Grafo Orientado Acíclico (DAG)

Um grafo direcionado sem ciclos.

## Referências

- [Wikipedia - Grafo](https://pt.wikipedia.org/wiki/Grafo)
- [GeeksforGeeks - Graph Data Structure And Algorithms](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/)
- Livro: "Introduction to Algorithms" - Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein.