import math
from collections import Counter


def make_total_entropy(first_topics):
    freq_first_topics = Counter(first_topics)
    total_entropy = 0

    for freq in freq_first_topics.values():
        total_entropy -= freq/len(first_topics) * math.log(freq/len(first_topics), 2)

    return total_entropy
