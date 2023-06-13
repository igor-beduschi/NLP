# Python activity for text normalization
# Igor Beduschi - 659318
# special characters remove, change accentuation to normal text, and text downcase.

import unicodedata as uni
import re
import csv

import nltk as tk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
import csv

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
with open("HO03/string_text.txt", "w+") as txt_file:
    txt_file.write(text)

print(normalization("It's true, Ms. Martha Töpfer! $3.00 on 3/21/2023 in cash for an ice-cream in the U.S. market? :-( #Truth"))
print("oi0")
with open("HO03/ShakespeareTokenized01.txt", "w+") as txt_file:
    tokenizado = " ".join(text.split())
    txt_file.write("["+tokenizado+"]")

##### HO03
#Removing stop words
stop_words = set(stopwords.words('english'))
words = tk.word_tokenize(tokenizado.lower())

stop_words = [word for word in words if word not in stop_words]

with open("HO03/ShakespeareTokenized01_SW.txt", "w+") as txt_file:
    txt_file.write("["+" ".join(stop_words)+"]")

#Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(word) for word in stop_words]

with open("HO03/ShakespeareTokenized01_00.txt", "w+") as txt_file:
    txt_file.write("["+" ".join(lemmatized)+"]")
#Stemming
stemmer = PorterStemmer()
stemmed = [stemmer.stem(word) for word in lemmatized]

with open("HO03/ShakespeareTokenized01_01.txt", "w+") as txt_file:
    txt_file.write("["+" ".join(stemmed)+"]")

#Snowball Stemming
snowball = SnowballStemmer('english')
snowball_stemmed = [snowball.stem(word) for word in stemmed]

with open("HO03/ShakespeareTokenized01_02.txt", "w+") as txt_file:
    txt_file.write("["+" ".join(snowball_stemmed)+"]")

#Analisy of vocabulary
lemma = []
stemmer = []
snow = []

def count_tokens(tokens, T):
    found = False
    for token in tokens:
        for row in T:
            if token in row:
                row[1] += 1
                found = True
        if(not found):
            T.append([token, 1, len(token)])
    return T

lemma = count_tokens(lemmatized, lemma)
stemmer = count_tokens(stemmed, stemmer)
snow = count_tokens(snowball_stemmed, snow)

lemmaFile = csv.writer(open("HO03/ShakespeareTokenized01_00.csv", "w+"))
lemmaFile.writerow(["Token", "Occurrences", "Size"])
for row in lemma:
  lemmaFile.writerow(row)

stemmerFile = csv.writer(open("HO03/ShakespeareTokenized01_01.csv", "w+"))
stemmerFile.writerow(["Token", "Occurrences", "Size"])
for row in stemmer:
  stemmerFile.writerow(row)

snowFile = csv.writer(open("HO03/ShakespeareTokenized01_02.csv", "w+"))
snowFile.writerow(["Token", "Occurrences", "Size"])
for row in snow:
  snowFile.writerow(row)

lemma_AvrgOc = 0
stemmer_AvrgOc = 0
snow_AvrgOc = 0
lemma_AvrSz = 0
stemmer_AvrSz = 0
snow_AvrSz = 0

for row in lemma:
    lemma_AvrgOc += row[1]
    lemma_AvrSz += row[2]
print(lemma_AvrgOc, len(lemma) )
lemma_AvrgOc /= len(lemma)
lemma_AvrSz /= len(lemma)


for row in stemmer:
    stemmer_AvrgOc += row[1]
    stemmer_AvrSz += row[2]
stemmer_AvrgOc /= len(stemmer)
stemmer_AvrSz /= len(stemmer)



for row in snow:
    snow_AvrgOc += row[1]
    snow_AvrSz += row[2]
snow_AvrgOc /= len(snow)
snow_AvrSz /= len(snow)

lenlemma = len(lemma)

# Write File
with open("HO03/ShakespeareTokenized01_VA.txt", "w+") as txt_file:
    txt_file.write(f"Lemmatization\n Size of Vocubulary: {lenlemma}")
    txt_file.write(f"\nOccurrences on average: {lemma_AvrgOc}")
    txt_file.write(f"\nSize on average: {lemma_AvrSz}")

    txt_file.write(f"\n\nPorter\n")
    txt_file.write(f"\nSize of Vocubulary: {len(stemmer)}")
    txt_file.write(f"\nOccurrences on average: {stemmer_AvrgOc}")
    txt_file.write(f"\nSize on average: {stemmer_AvrSz}")

    txt_file.write(f"\n\nSnowball\n")
    txt_file.write(f"\nSize of Vocubulary: {len(snow)}")
    txt_file.write(f"\nOccurrences on average: {snow_AvrgOc}")
    txt_file.write(f"\nSize on average: {snow_AvrSz}")
    