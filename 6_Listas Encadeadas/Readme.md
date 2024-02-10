# Limitações dos Vetores
Os vetores, apesar de sua simplicidade, apresentam algumas limitações que podem impactar o desempenho e a flexibilidade em determinados cenários:

1. **Busca Ineficiente em Vetores Não Ordenados:**
   - A operação de busca em vetores não ordenados pode ser morosa, especialmente em conjuntos de dados extensos, devido à necessidade de percorrer todo o vetor em busca do elemento desejado.

2. **Inserção Demorada em Vetores Ordenados:**
   - Em contrapartida, em vetores ordenados, a inserção pode ser uma operação lenta, pois requer o deslocamento de elementos para abrir espaço para o novo elemento, resultando em um aumento no tempo de execução.

3. **Remoção Ineficiente em Ambos os Casos:**
   - A remoção em vetores, independentemente de estarem ordenados ou não, pode ser uma operação demorada, principalmente quando a posição do elemento a ser removido não é conhecida antecipadamente.

4. **Imutabilidade do Tamanho do Vetor:**
   - Uma limitação significativa é a incapacidade de alterar dinamicamente o tamanho do vetor após a sua criação. Isso pode ser restritivo em situações em que a quantidade de elementos é desconhecida ou sujeita a alterações ao longo do tempo.

5. **Ocupação de Espaço Mesmo em Vetores Vazios:**
   - Mesmo quando estão vazios, os vetores ocupam espaço na memória, o que pode ser ineficiente em termos de utilização de recursos, especialmente em sistemas com restrições de memória.


# Listas encadeadas - Nós
   - Cada item de dados é incorporado em um nó
   - Cada nó possui uma referência para o próximo nó da lista
   - Um campo da própria lista contém uma referência para o primeiro nó
      <img src="images\Nó.png" width="500" height="200">

**Lista Encadeada Simples:**

Uma lista encadeada simples é uma estrutura de dados na qual cada elemento da lista é um nó que contém um valor e uma referência (ponteiro) para o próximo nó na sequência. O último nó geralmente aponta para `None`, indicando o final da lista.

<img src="images\simples.png" width="500" height="200">

*Pros:*
1. **Alocação Dinâmica de Memória:** A lista encadeada permite uma alocação dinâmica de memória, facilitando a inserção e remoção de elementos sem a necessidade de pré-alocação de espaço.
2. **Facilidade de Inserção e Exclusão:** Inserir ou excluir elementos no meio da lista é mais eficiente do que em arrays, pois envolve apenas a manipulação de ponteiros.
3. **Tamanho Dinâmico:** A lista pode crescer ou encolher dinamicamente conforme necessário, sem a necessidade de definir um tamanho fixo.

*Contras:*
1. **Acesso Sequencial:** O acesso a elementos em posições específicas requer percorrer a lista sequencialmente a partir do início, tornando as operações de busca menos eficientes.
2. **Overhead de Ponteiros:** Cada nó contém um ponteiro adicional, aumentando o overhead de armazenamento em comparação com estruturas de dados baseadas em arrays.

## As operações são:
   - Insere no inicio
   - Excluir do inicio
   - Mostrar lista
   - Pesquisar
   - Excluir da Posição
# _________________________________

# Lista Encadeada com Extremidades Duplas (Duplamente Encadeada)

Uma lista encadeada com extremidades duplas possui uma estrutura semelhante à lista encadeada simples, mas cada nó possui ponteiros para ambos o próximo e o nó anterior na sequência.

<img src="images\extremidadeDupla.png" width="500" height="200">

*Pros:*
1. **Acesso Bidirecional:** A capacidade de percorrer a lista em ambas as direções é uma vantagem em comparação com listas encadeadas simples, permitindo operações mais eficientes em certos cenários.
2. **Inserção e Exclusão Eficientes:** Inserir e excluir elementos no meio da lista é ainda mais eficiente do que em listas encadeadas simples, pois envolve a manipulação de dois ponteiros.
3. **Remoção Mais Eficiente do Último Elemento:** A remoção do último elemento é mais eficiente, pois o nó anterior já possui um ponteiro para `None`.

*Contras:*
1. **Maior Uso de Memória:** Os ponteiros adicionais aumentam o consumo de memória em comparação com listas encadeadas simples.
2. **Complexidade Adicional:** A implementação e manutenção de listas encadeadas duplamente encadeadas são mais complexas devido à gestão de dois conjuntos de ponteiros.

## As operações são:
   - Insere no inicio
   - *Insere no inicio* (adicional)
   - Excluir do inicio
   - Mostrar lista
   - Pesquisar
   - Excluir da Posição








**Escolha entre Lista Encadeada Simples e Duplamente Encadeada:**

- Se o acesso sequencial é mais comum e a economia de espaço é crucial, uma lista encadeada simples pode ser mais apropriada.
- Se operações de inserção e remoção frequentes no meio da lista são comuns, e o acesso bidirecional é vantajoso, a lista encadeada duplamente encadeada é uma escolha melhor.
- A escolha depende dos requisitos específicos de eficiência, uso de memória e padrões de acesso na aplicação.
