import math


def make_entropy(freq_first_topics, first_topics):
    entropy = 0

    for freq in freq_first_topics.values():
        entropy -= freq/len(first_topics) * math.log(freq/len(first_topics), 2)

    return entropy
