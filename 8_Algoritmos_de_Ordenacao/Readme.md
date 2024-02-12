# Algoritmos de Ordenação

Este README fornece uma visão geral dos seguintes algoritmos de ordenação:

- [Algoritmos de Ordenação](#algoritmos-de-ordenação)
  - [Bubble Sort](#bubble-sort)
  - [Selection Sort](#selection-sort)
  - [Insertion Sort](#insertion-sort)
  - [Shell Sort](#shell-sort)
  - [Merge Sort](#merge-sort)
  - [Quick Sort](#quick-sort)

## Bubble Sort

O **Bubble Sort** é um algoritmo simples de ordenação que percorre repetidamente a lista, compara elementos adjacentes e os troca se estiverem na ordem errada. A complexidade de tempo médio e pior caso é O(n^2).

Exemplo de uso: Ensino e aprendizado de algoritmos de ordenação em cursos introdutórios de ciência da computação.

[Link Explicativo](https://en.wikipedia.org/wiki/Bubble_sort)

## Selection Sort

O **Selection Sort** divide a lista em duas partes: uma parte ordenada e outra desordenada. Em cada iteração, o algoritmo encontra o menor elemento na parte desordenada e o troca com o primeiro elemento da parte ordenada. A complexidade de tempo médio e pior caso é O(n^2).

Exemplo de uso: Utilizado em situações onde a simplicidade do algoritmo é mais importante do que o desempenho, ou em casos específicos onde o conjunto de dados é pequeno.

[Link Explicativo](https://en.wikipedia.org/wiki/Selection_sort)

## Insertion Sort

O **Insertion Sort** constrói a lista ordenada um elemento de cada vez, pegando cada elemento e inserindo-o no local apropriado. A complexidade de tempo médio e pior caso é O(n^2).

Exemplo de uso: Muitas vezes usado em sistemas embarcados ou aplicações de tempo real, onde o tamanho dos dados é pequeno.

[Link Explicativo](https://en.wikipedia.org/wiki/Insertion_sort)

## Shell Sort

O **Shell Sort** é uma variação do Insertion Sort que compara elementos distantes antes de comparar elementos adjacentes. A complexidade de tempo médio é O(n log n), mas pode variar dependendo da sequência de lacunas utilizada.

Exemplo de uso: Implementações em bibliotecas padrão de linguagens de programação para ordenação de arrays.

[Link Explicativo](https://en.wikipedia.org/wiki/Shellsort)

## Merge Sort

O **Merge Sort** adota a estratégia de divisão e conquista. Divide a lista em duas partes, ordena cada parte e, em seguida, combina as partes ordenadas. A complexidade de tempo médio e pior caso é O(n log n).

Exemplo de uso: Implementações em algoritmos de ordenação padrão de linguagens de programação, como o método sorted() em Python.

[Link Explicativo](https://en.wikipedia.org/wiki/Merge_sort)

## Quick Sort

O **Quick Sort** também usa a estratégia de divisão e conquista. Escolhe um elemento como pivo, particiona a lista em elementos menores e maiores que o pivo, e repete o processo nas partes menores e maiores. A complexidade de tempo médio é O(n log n), mas pode degradar para O(n^2) no pior caso.

Exemplo de uso: Implementações em bibliotecas padrão de linguagens de programação e sistemas de gerenciamento de bancos de dados.

[Link Explicativo](https://en.wikipedia.org/wiki/Quicksort)
