from process.process_all_documents import process_all_documents
from stop_words import make_stop_words
from results import save_results
from gain.make_total_entropy import make_total_entropy
from gain.make_gain import make_gain
from threshold import apply_threshold
from data_set_path import get_data_set_path
from enums import OutputFilePath

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

global_vector_with_gains = {word: gain for word, gain in global_vector_with_gains.items() if gain > threshold}

global_vector = list(global_vector_with_gains.keys())

modified_documents = apply_threshold(documents, global_vector)

save_results(modified_documents, global_vector_with_gains, output_file_path2)
