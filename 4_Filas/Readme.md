# Fila em Python

## Descrição

Uma **fila** é uma estrutura de dados do tipo FIFO (First In, First Out), o que significa que o primeiro elemento adicionado é o primeiro a ser removido. Isso se assemelha a uma fila de espera, onde o primeiro indivíduo a chegar é o primeiro a ser atendido.

## Aplicações

As filas são frequentemente utilizadas em situações em que a ordem de chegada é importante e os elementos são processados na ordem em que foram adicionados. Algumas aplicações comuns incluem:

1. **Sistemas de Filas:** Em locais como bancos, supermercados e centros de atendimento, onde os clientes são atendidos com base na ordem de chegada.

2. **Impressão de Documentos:** Impressoras muitas vezes mantêm uma fila de documentos para serem impressos, processando-os na ordem em que foram enviados.

3. **Algoritmos de Busca em Grafos:** Em algoritmos de busca em largura (BFS), uma fila é utilizada para explorar os vizinhos de um nó antes de avançar para o próximo nível.

## Exemplo de Uso

Aqui está uma implementação simples de uma fila em Python:

```python
# Implementação de uma fila (FIFO - First In, First Out) em Python
class Fila:
    def __init__(self, capacidade):
        # Inicializa a fila com uma capacidade específica
        self.__capacidade = capacidade
        # Inicializa a frente e o final da fila como -1, indicando que está vazia
        self.__frente = -1
        self.__final = -1
        # Inicializa um array para armazenar os valores da fila
        self.__valores = np.empty(self.__capacidade, dtype=int)

    def __fila_cheia(self):
        # Verifica se a fila está cheia
        if self.__final == self.__capacidade - 1:
            return True
        else:
            return False
    
    def __fila_vazia(self):
        # Verifica se a fila está vazia
        if self.__frente == -1 or self.__frente > self.__final:
            return True
        else:
            return False  

    def enfileirar(self, valor):
        # Adiciona um elemento ao final da fila
        if self.__fila_cheia():
            print('A fila está cheia')
        else:
            if self.__frente == -1:
                self.__frente = 0
            self.__final += 1
            self.__valores[self.__final] = valor

    def desenfileirar(self):
        # Remove e retorna o elemento da frente da fila
        if self.__fila_vazia():
            print('A fila está vazia')
            return -1
        else:
            valor = self.__valores[self.__frente]
            self.__frente += 1
            return valor
    
    def ver_frente(self):
        # Retorna o valor na frente da fila sem removê-lo
        if self.__frente != -1:
            return self.__valores[self.__frente]
        else:
            return -1

# Exemplo de uso da fila
fila_exemplo = Fila(5)
fila_exemplo.enfileirar(10)
fila_exemplo.enfileirar(20)
fila_exemplo.enfileirar(30)

print('Frente da fila:', fila_exemplo.ver_frente())  # Output: 10

valor_removido = fila_exemplo.desenfileirar()
print('Valor removido:', valor_removido)  # Output: 10

print('Frente da fila após remoção:', fila_exemplo.ver_frente())  # Output: 20
```

Neste exemplo, criamos uma fila, enfileiramos alguns valores, desenfileiramos um valor e verificamos a frente da fila. As filas são utilizadas em uma variedade de contextos em programação, proporcionando uma abordagem eficiente para gerenciar elementos em uma ordem específica.