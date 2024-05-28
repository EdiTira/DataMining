import numpy as np


def apply_euclidian_distance(doc_rare_vector, input_rare_vector):
    all_indices = set(doc_rare_vector.keys()).union(set(input_rare_vector.keys()))

    squared_diff_sum = 0

    for index in all_indices:
        val1 = doc_rare_vector.get(index, 0)
        val2 = input_rare_vector.get(index, 0)
        squared_diff_sum += (val1 - val2) ** 2

    return np.sqrt(squared_diff_sum)


def make_similarity(documents, input_rare_vector):
    docs_with_similarity = []
    doc_no = 1
    for document in documents:
        document_rare_vector = document[0]
        similarity = apply_euclidian_distance(document_rare_vector, input_rare_vector)
        list_document = list(document)
        list_document.append(similarity)
        list_document.append('Document' + str(doc_no))
        document = tuple(list_document)
        docs_with_similarity.append(document)
        doc_no += 1
    return docs_with_similarity
