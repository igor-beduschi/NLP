# Python activity for text normalization
# Igor Beduschi - 659318
# special characters remove, change accentuation to normal text, and text downcase.

import unicodedata as uni
import re

import nltk
import nltk.tokenize as to
from nltk.tokenize import word_tokenize
import textblob as tb
import spacy
import gensim.utils as gensim
from keras.preprocessing.text import text_to_word_sequence as keraspptws

currency_finder_pattern = r'[$£€¥₹₽₿][0-9]+[.,][0-9]+'
date_finder_pattern = r'([0-9]{1,2})[/]([0-9]{1,2})[/]([0-9]{2,4})'


def normalization(text):
    text = uni.normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')
    # convert to lowercase
    text = text.lower()
    # add to normalized text string

    currency_matches = re.findall(currency_finder_pattern, text)
    date_matches = re.findall(date_finder_pattern, text)

    for match in currency_matches:
       # in this function, all the £€¥₹₽₿, was need to be in a reclace with a extend ascii character to work
       new_currency = re.sub(r"[.,]", "‡", match)
       new_currency = new_currency.replace("$", "Ž")
       text = text.replace(match, new_currency)

    for match in date_matches:
        data_match = f"{match[0]}/{match[1]}/{match[2]}"
        new_date = ''
        new_date += f'0{match[0]}¤' if len(match[0]) == 1 else f'{match[0]}¤'
        new_date += f'0{match[0]}¤' if len(match[1]) == 1 else f'{match[1]}¤'
        new_date += match[2]

        text = text.replace(data_match, new_date)

    # remove special characters
    text = re.sub(r"[^\w\s‡¤]", '', text)

    # return the comma and the $ to the currency, if i use all the £€¥₹₽₿, more replaces functions is needed
    text = text.replace("‡", ",")
    text = text.replace("Ž", "$")
    text = text.replace("¤", "/")

    return text

# Read text from file, and close after
with open('datasets/Shakespeare.txt') as s:
    text = s.read()
    # normalize
    text = normalization(text)

# Write normalized text to file
with open("HO02/string_text.txt", "w+") as txt_file:
    txt_file.write(text)

print(normalization("It's true, Ms. Martha Töpfer! $3.00 on 3/21/2023 in cash for an ice-cream in the U.S. market? :-( #Truth"))

with open("HO02/ShakespeareTokenized01.txt", "w+") as txt_file:
    txt_file.write("["+", ".join(text.split())+"]")

with open("HO02/ShakespeareTokenized02.txt", "w+") as txt_file:
    txt_file.write("[" + ", ".join(to.word_tokenize(text))+"]")

with open("HO02/ShakespeareTokenized03.txt", "w+") as txt_file:
    txt_file.write("[" + ", ".join(to.TreebankWordTokenizer().tokenize(text))+"]")

with open("HO02/ShakespeareTokenized04.txt", "w+") as txt_file:
    txt_file.write("[" + ", ".join(to.WordPunctTokenizer().tokenize(text))+"]")

with open("HO02/ShakespeareTokenized05.txt", "w+") as txt_file:
    txt_file.write("[" + ", ".join(to.TweetTokenizer().tokenize(text))+"]")

with open("HO02/ShakespeareTokenized06.txt", "w+") as txt_file:
    txt_file.write("[" + ", ".join(to.MWETokenizer().tokenize(word_tokenize(text)))+"]")

with open("HO02/ShakespeareTokenized07.txt", "w+") as txt_file:
    txt_file.write("[" + ", ".join(tb.TextBlob(text).words)+"]")

with open("HO02/ShakespeareTokenized08.txt", "w+") as txt_file:
    nlp = spacy.load("en_core_web_sm")
    tokanizer = [token.text for token in nlp(text)]
    txt_file.write("[" + ", ".join(word_tokenize(text))+"]")

with open("HO02/ShakespeareTokenized09.txt", "w+") as txt_file:
    txt_file.write(("[" + ", ".join(list(gensim.tokenize(text)))+"]"))

with open("HO02/ShakespeareTokenized10.txt", "w+") as txt_file:
    txt_file.write("[" + ", ".join(keraspptws(text))+"]")
