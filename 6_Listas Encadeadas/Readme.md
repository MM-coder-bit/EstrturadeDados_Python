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

# Lista encadeadas simples
## As operações contidas neste modelo são:
   - Insere no inicio
   - Excluir do inicio
   - Mostrar lista
   - Pesquisar
   - Excluir da Posição

