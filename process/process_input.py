import re
from nltk.stem.porter import PorterStemmer


def process_input(input_document, global_vector):
    with open(input_document, 'r') as file:
        text = file.read()
    stemmer = PorterStemmer()
    text = re.sub(r'[\W\d]+', ' ', text.lower())
    words = text.split()

    stemmed_words = []

    for word in words:
        stemmed_word = stemmer.stem(word)
        stemmed_words.append(stemmed_word)

    rare_vector_input = {}

    for word in global_vector:
        if word in stemmed_words:
            rare_vector_input[global_vector.index(word)] = 1
        else:
            rare_vector_input[global_vector.index(word)] = 0

    return rare_vector_input
