# Basic Concepts

## Text
Text is anything that can be read. It is a symbolic arrangement of letters in a piece of writing, a coherent set of signs that transmits some kind of informative message.

```
"After you have chosen your words, they must be weaved together into a fine and delicate fabric."
Institutio Oratoria, Quintilian (Roman Educator), 95 BC
```

> From Latin: **Textum** = **Fabric**

> See in [Wikipedia](https://en.wikipedia.org/wiki/Text_(literary_theory)).

## Text Mining
Deriving high-quality information from text
  - High-quality -> relevance, novelty or interest
  - Discovery by computer of new, previously unknown information, by automatically extracting information from different written resources (text)
  - Structuring the input text -> Derive patterns within the structured data -> Evaluation and interpretation of the output
  - Turn text into data for analysis, via application of natural language processing (NLP) and different types of analytical methods

> Synonyms: Text Data Mining (TDM), Text Analytics
>
> Related Terms: Data Mining, Knowledge Discovery

> See in [Wikipedia](https://en.wikipedia.org/wiki/Text_mining).


## Text Normalization
Transforming text into a single canonical form.
> Synonyms: Canonicalization
>
> Related Terms: Morphology Transformation

Challenges:
  - anti-discriminatory, antidiscriminatory -> antidiscriminatory
  - pêra, pera -> pera
  - black, Black -> black
  - CAT, cat -> cat
  - colour, color -> color
  - 2/3/2021 -> Mar, 2 2021
  - 230.423 203,423 -> 230423
  - Rindfleischetikettierungsueberwachungsaufgabenuebertragungsgesetz -> lei que delega a monitorização da carne de vaca

It frequently evolves case-transformation, punctuation, accents and special characters removal

Morfologia -> Composição textual   window, window + ing (ação), window + s (plural)

Sintaxe -> Composição gramatical do texto    Substantivo? Verbo? Adjetivo?

Semântica -> Significado dos componentes textuais -> conceito, ideia

Python Libraries: unidecode, re

> See in [Book Chapter](https://nlp.stanford.edu/IR-book/html/htmledition/normalization-equivalence-classing-of-terms-1.html).


## Text Segmentation
Non-trivial problem of dividing a string of written language into its components.

  - Morphological Segmentation: String -> Morphemes
  - Word Segmentation: String -> words
  - Intent Segmentation: String -> 2 or more group of words
  - Sentence Segmentation: String -> sentences
  - Paragraph Segmentation: String -> paragraphs
  - Topic Segmentation: String -> topics (groups of sentences on the same topic)

> See in [Wikipedia](https://en.wikipedia.org/wiki/Text_segmentation#:~:text=Text%20segmentation%20is%20the%20process,subject%20of%20natural%20language%20processing).

> See in [Topic Segmentation](https://www.assemblyai.com/blog/text-segmentation-approaches-datasets-and-evaluation-metrics/).

## Text Tokenization
It's a [Text Segmentation](#text-segmentation) problem of breaking the raw text into small chunks, such as words, terms, sentences, symbols, or some other meaningful elements called tokens.

A tokenizer breaks unstructured data and natural language text into chunks of discrete elements, where token occurrences can be used as a vector representing text. This turns text into a numerical data structure suitable for NLP and machine learning.


Challenges:
  - The boundary of a word varies in different languages;
  - Form variations (It is and It's)

Approaches:
  - White Space Tokenization
  - Rule Based Tokenization (Dictionary Based Tokenization, Regular Expression Tokenization)
  - Penn TreeBank Tokenization
  - Spacy Tokenizer
  - Moses Tokenizer
  - Subword Tokenization (BPE, WordPiece, Unigram Language Model)

Python Libraries:
  - NLTK: WhitespaceTokenizer, word_tokenize, TreebankWordTokenizer, wordpunct_tokenize, TweetTokenizer, MWETokenizer
  - TextBlob
  - spaCy
  - Gensim
  - Keras


  - nltk
    from nltk.tokenize import WhitespaceTokenizer
    from nltk.tokenize import word_tokenize
    from nltk.tokenize.treebank import TreebankWordTokenizer
    from nltk.tokenize import wordpunct_tokenize
    from nltk.tokenize import TweetTokenizer
    from nltk.tokenize import MWETokenizer
    from textblob import TextBlob
  - textblob
  - spacy
  - gensim
    from gensim.utils import tokenize

> See in Book [Chapter](https://nlp.stanford.edu/IR-book/html/htmledition/tokenization-1.html).


## Text Lematization

Python Libraries: NLTK (WordNetLemmatizer)

## Text Stemming
Python Libraries: NLTK (PorterStemmer, SnowballStemmer)

## Stop Words
Python Libraries: NLTK (stopwords)

## Text Representation

Texto 1
  Raw: "Men, plans, an astonishing canal - Panama."
  Processed: "man plan astonish canal panama"

Texto 2
  Raw: "Men work in canal suez man."
  Processed: "man work canal suez man"

V = {astonish, canal, man, panama, plan, suez, work}

### ONE-HOT ENCODING

        0 1 2 3 4 5 6
v1 = {  1 1 1 1 1 0 0 }
v2 = {  0 1 1 0 0 1 1 }

Positivo:
1. Simples de computar

Negativo:
1. Vocabulário tende a ser muito grande, gerando vetores grandes e esparsos
2. Perco a ordem com que os termos ocorreram nos textos
3. Eu não tenho a frequência de ocorrência dos termos nos textos


### COUNT VECTORS

0 1 2 3 4 5 6
v1 = {  1 1 1 1 1 0 0 }
v2 = {  0 1 2 0 0 1 1 }

Positivo:
1. Simples de computar

Negativo:
1. Vocabulário tende a ser muito grande, gerando vetores grandes e esparsos
2. Perco a ordem com que os termos ocorreram nos textos


### TF-IDF (Salton)

TF = Term Frequency -> # ocorrências do termo no texto
IDF = Inverted Document Frequency -> quantos textos diferentes da coleção o termo ocorreu

TF = log(1 + f_t,d)
IDF = log (N/(1 + n_t)) + 1
TF-IDF = TF * IDF

astonish -> TF = log(1+1) = 1; IDF = log(2/(1+1)) + 1 = 1; TF-IDF = 1

0 1 2 3 4 5 6
v1 = {  1 1 1 1 1 0 0 }
v2 = {  0 1 2 0 0 1 1 }

Positivo:
1. Simples de computar
2. Capto relevância do termo no documento e na coleção

Negativo:
1. Vocabulário tende a ser muito grande, gerando vetores grandes e esparsos
2. Perco a ordem com que os termos ocorreram nos textos



One-hot encoding, Count Vector e TF-IDF -> BoW (Bag of Words)



### CO-OCCURRENCE VECTORS
                      astonish  canal man panama  plan  suez  work
astonish              1         1     0   0       1     0     0
canal                           1
man                                   1
panama                                    1
plan                                              1
suez                                                    1
work                                                          1

Janela = 1

Positivo:
1. Capto a vizinhança de palavras -> semântica
2. Apropriado para aplicação de técnicas de redução de dimensionalidade

Negativo:
1. Computação cara -> Vocabulário tende a ser muito grande, gerando vetores grandes e esparsos
2. Matrizes com dimensionalidade muito alta



### N-GRAMS

n-gram -> conjuntos de n termos
2-grams

V = {astonish, canal, man, panama, plan, suez, work}

man plan
plan astonish
astonish canal
canal panama
man work
work canal
canal suez
suez man


Positivo:
1. Capto relevância do n-gram no documento e na coleção
2. Capto vizinhança, semântica

Negativo:
1. Computação cara -> Vocabulário >>
2. Vocabulário tende a ser muito grande, gerando vetores grandes e esparsos



### Word Embeddings (Word2Vec, FastText, Glove)

Desejo:
1. Gerar vetores densos (dimensionalidade controlada)
2. Fáceis de serem gerados (custo baixo)
3. Semânticamente ricos

Explicabilidade

v1 = {  0.3234 0.4323 0.5234 0.8456 0.6345 0.1234 0.5348 }

Python
sklearn -> CountVectorizer()

> See [Examples](https://towardsdatascience.com/text-data-representation-with-one-hot-encoding-tf-idf-count-vectors-co-occurrence-vectors-and-f1bccbd98bef).

## Text Similarity
Similaridade: quão parecidos ou diferentes 2 objetos são?

Se objetos são representados como vetores então podemos considerar **similaridade** textual como **distância** entre vetores

Vetores: features de objetos (texto)
Distância: número real no intervalo [0, 1]

Qualidade da representação vetorial impacta significativamente na medida de similaridade

Métricas de Similaridade:
- Jaccard Index (Jaccard Distance)
- Minkowski Distance
  - Manhattan Distance
  - Euclidean Distance
- Similaridade por Coseno (Cosine Similarity)

Embedding de Objetos:
- BoW (One-Hot Encoding)
- BoW (Count Vectors)
- BoW (TF-IDF)
- BoW (n-grams)
- Co-occurrence Vectors
- Neural Text Embeddings (Word2Vec)

### Jaccard Distance
Baseada em teoria de conjuntos
Tamanho da intersecção / Tamanho da União

### Euclidean Distance (L2)

[1, 2, 4]
[2, 1, 3]

RAIZ[(1-2)^2 + (2-1)^2 + (4-3)^2] = RAIZ(1 + 1 + 1) = 1,732050


### Manhattan Distance (L1)

(1-2) + (2-1) + (4-3) = 3

### Minkowski Distance (L3, L4...)
p=1 -> Manhattan Distance
p=2 -> Euclidean Distance
p > 2

### Cosine Similarity
[1, 2, 4]
[2, 1, 3]

Numerador -> 1*2 + 2*1 + 4*3 = 16
Denominador -> 294
  Fator 1 -> RAIZ(1^2 + 2^2 + 4^2) = 21
  Fator 2 -> RAIZ(2^2 + 1^2 + 3^2) = 14

  16/294 = 0,0544
