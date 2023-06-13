from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from gensim.models import Word2Vec
from collections import defaultdict
import numpy as np
import unicodedata as uni
import re

# Load the 20newsgroups dataset
newsgroups = fetch_20newsgroups(subset='all')
data = newsgroups.data[:1000]

np.set_printoptions(threshold= np.inf, suppress=True)

def file_writer(data, filename):
    with open("HO04/"+filename, 'w') as f:
        f.write(data)

def normalizer(text):
    text = uni.normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')
    text = text.lower()
    text = re.sub(r"[^\w\s]", '', text)

    return text

def one_hot_encoding(normalized_data):
    vectorizer = CountVectorizer(binary= True, max_features=1000)
    vectorizer.fit(normalized_data)
    vector = vectorizer.transform(normalized_data)

    return str(vector.toarray())

def count_vector(normalized_data):
    vectorizer = CountVectorizer(binary= False, max_features=1000)
    vectorizer.fit(normalized_data)
    vector = vectorizer.transform(normalized_data)

    return str(vector.toarray())

def tf_idf(normalized_data):
    vectorizer = TfidfVectorizer(max_features=1000)
    vectorizer.fit(normalized_data)
    vector = vectorizer.transform(normalized_data)

    return str(vector.toarray())

def two_grams_counter(normalized_data):
    vectorizer = CountVectorizer(binary= True, ngram_range=(2,2), max_features=1000)
    vectorizer.fit(normalized_data)
    vector = vectorizer.transform(normalized_data)

    return str(vector.toarray())

# https://towardsdatascience.com/word-vectors-intuition-and-co-occurence-matrixes-a7f67cae16cd
def co_occurrence_matrix(normalized_data):
    vectorizer_pair = CountVectorizer(binary= True, ngram_range=(2,2), max_features=1000)
    vectorizer_pair.fit(normalized_data)
    vector_pair = vectorizer_pair.transform(normalized_data).toarray()

    vector_pair_sum = np.sum(vector_pair, axis=0)

    vector_pair_list = [vector.split(" ") for vector in vectorizer_pair.get_feature_names_out()]
    vocabulary_append = list(
        {word for vector in vector_pair_list for word in vector}
    )

    vectorizer = CountVectorizer(binary= True, vocabulary=vocabulary_append)
    vectorizer.fit(normalized_data)
    
    co_ocurrence_matrix = np.zeros((len(vocabulary_append), len(vocabulary_append)))

    for vector in vector_pair_list:
        i1 = vectorizer.vocabulary_[vector[0]]
        i2 = vectorizer.vocabulary_[vector[1]]
        t = vector_pair_list.index(vector)
        co_ocurrence_matrix[i1][i2] += 1 * t
        if i1 != i2:
            co_ocurrence_matrix[i2][i1] += 1 * t
        
    return str(co_ocurrence_matrix.astype(int))

def word2vec(normalized_data):
    vectorizer = CountVectorizer(binary= True, max_features=1000)
    analyzer = vectorizer.build_analyzer()
    corpus = [analyzer(text) for text in normalized_data]

    model = Word2Vec(corpus, min_count=1, max_vocab_size=1000)
    vectorizer = [model.wv[key] for key in model.wv.index_to_key]
    return str(vectorizer)

if __name__ == '__main__':
    normalized_data = [normalizer(input) for input in data]

    file_writer(one_hot_encoding(normalized_data),"20News_01.txt")
    file_writer(count_vector(normalized_data),"20News_02.txt")
    file_writer(tf_idf(normalized_data),"20News_03.txt")
    file_writer(two_grams_counter(normalized_data),"20News_04.txt")
    file_writer(co_occurrence_matrix(normalized_data),"20News_05.txt")
    file_writer(word2vec(normalized_data),"20News_06.txt")