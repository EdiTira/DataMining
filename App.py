from process.process_all_documents import process_all_documents
from stop_words import make_stop_words
from results import save_results
from collections import Counter
from gain.make_entropy import make_entropy

stop_words = make_stop_words()

directory_path = '../DataMining/dataSet/Reuters_34/Training'

output_file_path = 'output.txt'

global_vector, documents, first_topics = process_all_documents(directory_path, stop_words)

freq_first_topics = Counter(first_topics)

entropy = make_entropy(freq_first_topics, first_topics)

print(first_topics)

print(len(global_vector))

save_results(documents, global_vector, output_file_path)
