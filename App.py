from process.process_all_documents import process_all_documents
from stop_words.make_stop_words import make_stop_words
from results.save_results import save_results

stop_words = make_stop_words()

directory_path = '../DataMining/dataSet/Reuters_7083'

output_file_path = 'output.txt'

global_vector, documents = process_all_documents(directory_path, stop_words)

print(len(global_vector))

save_results(documents, global_vector, output_file_path)
