import re
from collections import Counter
from nltk.stem.porter import PorterStemmer


def process_text(text, stop_words, global_vector):
    stemmer = PorterStemmer()
    text = re.sub(r'[\W\d]+', ' ', text.lower())
    words = text.split()

    stemmed_words = []
    for word in words:
        if word not in stop_words and len(word) > 2:
            stemmed_word = stemmer.stem(word)
            stemmed_words.append(stemmed_word)
            if stemmed_word not in global_vector:
                global_vector.append(stemmed_word)

    rare_vector = {}
    for word, freq in Counter(stemmed_words).items():
        rare_vector[global_vector.index(word)] = freq

    return rare_vector
