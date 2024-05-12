from entropy.make_total_occurrences import make_total_occurrences
from entropy.make_entropy import make_entropy


def save_results(documents, global_vector, output_file_path):
    total_occurrences = make_total_occurrences(global_vector)

    with open(output_file_path, 'w') as f:
        for word in global_vector:
            entropy = make_entropy(global_vector[word], total_occurrences)
            f.write(f"@attribute {word}, {entropy}\n")
        f.write("@data\n")

        for freq_vector, topics in documents:
            vector_str = " ".join([f"{global_vector[word]}:{freq}" for word, freq in freq_vector.items()])
            topics_str = " ".join(topics)
            f.write(f"{vector_str} # {topics_str}\n")
