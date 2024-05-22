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
            global_vector.add(stemmed_word)

    return Counter(stemmed_words)
