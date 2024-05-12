import os
from process import process_document
from collections import Counter


def process_all_documents(directory, stop_words):
    global_vector = Counter()
    documents = []

    for file_name in os.listdir(directory):
        if file_name.endswith('.XML'):
            file_path = os.path.join(directory, file_name)
            freq_vector, topics = process_document(file_path, stop_words)

            global_vector.update(freq_vector)
            documents.append((freq_vector, topics))

    return global_vector, documents
