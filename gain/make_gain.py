import math


def make_gain(documents, global_vector, total_entropy):
    no_of_documents = len(documents)

    global_vector_with_gains = {}

    for word in global_vector:
        topic_freq_exist = {}
        topic_freq_no_exist = {}
        word_appearances = 0
        for document in documents:
            rare_vector = document[0]
            first_topic = document[1][0]
            if global_vector.index(word) in rare_vector:
                word_appearances += 1
                topic_freq_exist[first_topic] = topic_freq_exist.get(first_topic, 0) + 1
            else:
                topic_freq_no_exist[first_topic] = topic_freq_no_exist.get(first_topic, 0) + 1

        word_no_appearances = no_of_documents - word_appearances

        attribute_entropy_exist = make_attribute_entropy(topic_freq_exist, word_appearances)
        attribute_entropy_no_exist = make_attribute_entropy(topic_freq_no_exist, word_no_appearances)

        gain = total_entropy - (word_appearances / no_of_documents * attribute_entropy_exist + word_no_appearances / no_of_documents * attribute_entropy_no_exist)

        global_vector_with_gains[word] = gain

    return global_vector_with_gains


def make_attribute_entropy(topic_freq, appearances):
    attribute_entropy = 0.0

    for freq in topic_freq.values():
        attribute_entropy -= freq / appearances * math.log(freq / appearances, 2)

    return attribute_entropy
