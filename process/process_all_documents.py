import os
from process.process_document import process_document


def process_all_documents(directory, stop_words):
    global_vector = set()
    documents = []
    first_topics = []

    for file_name in os.listdir(directory):
        if file_name.endswith('.XML'):
            file_path = os.path.join(directory, file_name)
            freq_vector, topics = process_document(file_path, stop_words, global_vector, first_topics)

            documents.append((freq_vector, topics))

    return global_vector, documents, first_topics
