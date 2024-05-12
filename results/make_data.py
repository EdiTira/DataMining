def make_data(documents, global_vector, file):
    for freq_vector, topics in documents:
        vector_str = " ".join([f"{global_vector[word]}:{freq}" for word, freq in freq_vector.items()])
        topics_str = " ".join(topics)
        file.write(f"{vector_str} # {topics_str}\n")

