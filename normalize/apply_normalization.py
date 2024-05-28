def apply_normalization(documents, global_vector):
    for word in global_vector:
        for document in documents:
            rare_vector = document[0]
            if global_vector.index(word) in rare_vector:
                rare_vector[global_vector.index(word)] = 1
            else:
                rare_vector[global_vector.index(word)] = 0

    return documents
