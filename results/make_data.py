def make_data(documents, file):
    document_no = 1
    for rare_vector, topics in documents:
        vector_str = " ".join([f"{index}:{freq}" for index, freq in rare_vector.items()])
        topics_str = " ".join(topics)
        file.write(f"D{document_no} # {vector_str} # {topics_str}\n")
        document_no += 1

