# Pilha em Python

## Descrição

Uma **pilha** é uma estrutura de dados do tipo LIFO (Last In, First Out), o que significa que o último elemento adicionado é o primeiro a ser removido. Isso se assemelha a uma pilha de pratos, onde você adiciona um prato ao topo e remove o prato do topo.

## Aplicações

As pilhas são comumente utilizadas em situações em que a ordem de processamento é relevante, e o último item adicionado deve ser o primeiro a ser processado. Algumas aplicações comuns incluem:

1. **Controle de chamadas de função:** As pilhas são usadas na execução de programas para controlar a ordem de chamadas de função e alocar espaço de memória para variáveis locais.

2. **Navegação em histórico:** Os navegadores da web usam pilhas para armazenar o histórico de páginas visitadas. Cada nova página é adicionada ao topo da pilha.

3. **Desfazer (Undo):** Aplicações como editores de texto e software gráfico utilizam pilhas para implementar a funcionalidade de desfazer. Cada ação realizada é empilhada, permitindo desfazer as ações na ordem inversa.

## Exemplo de Uso

A seguir, temos uma implementação simples de uma pilha em Python:

```python
# Implementação de uma pilha (LIFO - Last In, First Out) em Python
class Pilha:
    def __init__(self, capacidade):
        # Inicializa a pilha com uma capacidade específica
        self.__capacidade = capacidade
        # Inicializa o topo da pilha como -1, indicando que está vazia
        self.__topo = -1
        # Inicializa um array para armazenar os valores da pilha
        self.__valores = np.empty(self.__capacidade, dtype=int)

    def __pilha_cheia(self):
        # Verifica se a pilha está cheia
        if self.__topo == self.__capacidade - 1:
            return True
        else:
            return False
    
    def __pilha_vazia(self):
        # Verifica se a pilha está vazia
        if self.__topo == -1:
            return True
        else:
            return False  

    def empilhar(self, valor):
        # Adiciona um elemento ao topo da pilha
        if self.__pilha_cheia():
            print('A pilha está cheia')
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor

    def desempilhar(self):
        # Remove e retorna o elemento do topo da pilha
        if self.__pilha_vazia():
            print('A pilha está vazia')
            return -1
        else:
            valor = self.__valores[self.__topo]
            self.__topo -= 1
            return valor
    
    def ver_topo(self):
        # Retorna o valor no topo da pilha sem removê-lo
        if self.__topo != -1:
            return self.__valores[self.__topo]
        else:
            return -1

# Exemplo de uso da pilha
pilha_exemplo = Pilha(5)
pilha_exemplo.empilhar(10)
pilha_exemplo.empilhar(20)
pilha_exemplo.empilhar(30)

print('Topo da pilha:', pilha_exemplo.ver_topo())  # Output: 30

valor_removido = pilha_exemplo.desempilhar()
print('Valor removido:', valor_removido)  # Output: 30

print('Topo da pilha após remoção:', pilha_exemplo.ver_topo())  # Output: 20
```

Neste exemplo, criamos uma pilha, empilhamos alguns valores, removemos um valor e verificamos o topo da pilha. Este é apenas um exemplo básico, e as pilhas podem ser aplicadas em uma variedade de contextos em programação.