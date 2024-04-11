import re
from collections import Counter
from nltk.stem.porter import PorterStemmer


def process_text(text, stop_words):
    stemmer = PorterStemmer()
    text = re.sub(r'\W+', ' ', text.lower())
    words = text.split()

    words = [stemmer.stem(word) for word in words if word not in stop_words and len(word) > 2]

    return Counter(words)