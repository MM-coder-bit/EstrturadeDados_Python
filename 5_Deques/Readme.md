# Deque em Python

## Descrição

Um **Deque** (Double-Ended Queue) é uma estrutura de dados que combina características de uma pilha (LIFO - Last In, First Out) e uma fila (FIFO - First In, First Out). Isso significa que você pode adicionar e remover elementos tanto no início quanto no final da estrutura.

## Aplicações

O Deque é especialmente útil em situações em que é necessário acessar rapidamente tanto o início quanto o final da coleção de dados. Algumas aplicações comuns incluem:

1. **Processamento em Lote:** Quando os dados precisam ser processados em lotes e a ordem de chegada é importante.

2. **Algoritmos de Busca de Caminho:** Em algoritmos como BFS (Breadth-First Search), onde é necessário explorar os vizinhos de um nó em ambas as direções.

3. **Manejo de Tarefas em Paralelo:** Em sistemas concorrentes, onde as tarefas podem ser adicionadas ou removidas tanto no início quanto no final.

## Vantagens do Deque

1. **Acesso Eficiente:** O Deque permite um acesso eficiente tanto no início quanto no final, tornando-o ideal para casos em que a ordem de processamento pode variar.

2. **Operações Rápidas:** Adicionar ou remover elementos no início ou no final de um deque é uma operação de tempo constante O(1).

3. **Flexibilidade:** A flexibilidade do Deque o torna uma escolha versátil em comparação com estruturas de dados mais especializadas.

## Exemplo de Uso

Aqui está uma implementação simples de um deque em Python:

```python
# Implementação de um Deque em Python
from collections import deque

# Criar um deque vazio
deque_exemplo = deque()

# Adicionar elementos no final
deque_exemplo.append(10)
deque_exemplo.append(20)
deque_exemplo.append(30)

# Adicionar elementos no início
deque_exemplo.appendleft(5)
deque_exemplo.appendleft(15)

# Remover elemento do final
elemento_removido_final = deque_exemplo.pop()

# Remover elemento do início
elemento_removido_inicio = deque_exemplo.popleft()

# Imprimir o deque resultante
print(deque_exemplo)  # Output: deque([15, 5, 10, 20])

print('Elemento removido do final:', elemento_removido_final)  # Output: 30
print('Elemento removido do início:', elemento_removido_inicio)  # Output: 5
```

Neste exemplo, usamos a biblioteca padrão `collections` para criar e manipular um deque. A flexibilidade do deque permite adicionar e remover elementos eficientemente em ambas as extremidades da estrutura.