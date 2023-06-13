# Text Clustering

Process of separating different parts of data based on common characteristics
EDA = Exploratory Data Analysis

Algoritmos não-supervisionados para entender a natureza dos dados, como eles se relacionam e comportam.

sklearn = dezenas de algoritmos de clustering

K-Means -> Particionamento
  - Ponto Positivo:
    - Simples e rápido
  - Pontos Negativos:
    - Definir o K
    - Baseado em centróides (espaços circulares)

Affinity Propagation -> Particionamento
  - Pontos Negativos:
    - Baseado em Votação -> Privilegia centróides
    - Mais lento
  - Ponto Positivo:
    - Não preciso definir o K -> Votação

Mean Shift -> Método estatístico baseado em função de densidade
- Pontos Negativos:
  - Baseado em centróides (espaços circulares)
  - Mais lento
- Ponto Positivo:
  - Não preciso definir o K

Spectral Clustering -> Método baseado em grafos (distância)
Generalização do K-Means
Transformar um espaço de entrada em um espaço mais distribuído de saída
- Pontos Negativos:
  - Computacionalmente mais caro comparado ao K-Means
- Ponto Positivo:
  - Não é baseado em centróide, é capaz de detectar clusters mais difíceis de serem observados a olho nu
  - Mais estável

Agglomerative Clustering -> Binary Trees
Geralmente usa centróide como medida de distância

- Pontos Negativos:
  - Computacionalmente barato
- Ponto Positivo:
  - Muito estável

DBSCAN -> Baseado em medidas de densidade
Transformar um espaço de entrada em um espaço mais distribuído de saída
Não baseado em centróide

- Pontos Negativos:
  - Sensível aos parâmetros de distância
- Ponto Positivo:
  - Computacionalmente muito barato -> volume gigante de dados
  - Muito estável
  - Capaz de detectar clusters mais difíceis de serem observados a olho nu

HDBSCAN ->  Varia a forma de computar densidade
- Pontos Negativos:
  - Computacionalmente mais caro que o DBSCAN
- Ponto Positivo:
  - Muito estável
  - Ainda mais capaz de detectar clusters mais difíceis de serem observados a olho nu

  ## Example Notebook

  [https://colab.research.google.com/drive/1eBfsVgY75C89Gb-4BdJQ1m1EFOGzIMkw](https://colab.research.google.com/drive/1eBfsVgY75C89Gb-4BdJQ1m1EFOGzIMkw)
