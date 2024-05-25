def apply_threshold(documents, global_vector):
    modified_documents = []

    for document in documents:
        rare_vector = document[0]
        topics = document[1]
        new_rare_vector = {}
        for word in global_vector:
            index = global_vector.index(word)
            if index in rare_vector:
                new_rare_vector[index] = rare_vector[index]
        modified_documents.append((new_rare_vector, topics))

    return modified_documents
