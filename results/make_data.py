def make_data(documents, global_vector, file):
    global_vector_list = list(global_vector)
    document_no = 1
    for freq_vector, topics in documents:
        vector_str = " ".join([f"{global_vector_list.index(word)}:{freq}" for word, freq in freq_vector.items()])
        topics_str = " ".join(topics)
        file.write(f"D{document_no} # {vector_str} # {topics_str}\n")
        document_no += 1

