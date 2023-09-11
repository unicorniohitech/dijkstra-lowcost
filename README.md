# Menor preço - Algoritmo De Dijkastra

Indo por um caminho voltado para a urbanização, foi explorado uma estrutura de dados em grafo, obtida de uma base da dados com todas as conexões intermunicipais nacionais. Depois de um tratamento de dados, o escopo fixou-se no estado de Minas Gerais 770 municípios e 3472 conexões. 
Então, foi desenvolvido, após o tratamento de dados utilizando a biblioteca Pandas, um algoritmo que busca o caminho mais barato, utilizando o transporte público, e o mais curto entre as duas cidades informadas pelo usuário.

O algoritmo em questão foi o algoritmo de Dijkastra, sendo este muito eficiente,tendo seu funcionamento através da busca do caminho mais curto entre dois vértices em um grafo ponderado e direcionado, realizando esse processo e atribuindo um peso para cada aresta, ele mantém uma estrutura que comporta nós visualizados e outra com o oposto, por fim, através de heap ele trata de atualizar as distâncias frequentemente.

A Base de dados foi obtida no seguinte link: https://www.ibge.gov.br/geociencias/cartas-e-mapas/redes-geograficas/15798-regioes-de-influencia-das-cidades.html?edicao=28033&t=downloads
