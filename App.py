from process import process_all_documents, process_input
from stop_words import make_stop_words
from results import save_results
from gain import make_gain, make_total_entropy
from threshold import apply_threshold
from data_set_path import get_data_set_path
from enums import OutputFilePath
from normalize import apply_normalization
from similarity import make_similarity

stop_words = make_stop_words()

data_set_choice = int(input('Choose the data set: 1 - Training_34, 2 - Testing, 3 - Reuters_7083: '))

data_set_path = get_data_set_path(data_set_choice)

output_file_path = OutputFilePath.OUTPUT_PATH_1.value
output_file_path2 = OutputFilePath.OUTPUT_PATH_2.value

global_vector, documents, first_topics = process_all_documents(data_set_path, stop_words)

total_entropy = make_total_entropy(first_topics)

global_vector_with_gains = make_gain(documents, global_vector, total_entropy)

save_results(documents, global_vector_with_gains, output_file_path)

threshold = float(input('Enter the threshold: '))

if threshold == 0:
    normalized_documents = apply_normalization(documents, global_vector)
    save_results(normalized_documents, global_vector_with_gains, output_file_path2)
    input_document_path = "input/Interogari de test pentru setul cu 34 documente.txtText.txt"
    rare_vector_input = process_input(input_document_path, global_vector)
    docs_with_similarity = make_similarity(normalized_documents, rare_vector_input)
    docs_with_similarity = sorted(docs_with_similarity, key=lambda x: x[2], reverse=True)
    for doc in docs_with_similarity:
        print(doc[3] + ' - ' + str(doc[2]))


global_vector_with_gains = {word: gain for word, gain in global_vector_with_gains.items() if gain > threshold}

threshold_documents = apply_threshold(documents, list(global_vector_with_gains.keys()))

save_results(threshold_documents, global_vector_with_gains, output_file_path2)




