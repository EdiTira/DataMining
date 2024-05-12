import math
from entropy import make_word_proportion


def make_entropy(word, total_occurrences):
    word_proportion = make_word_proportion(word, total_occurrences)

    return -1 * word_proportion * math.log(word_proportion, 2)
