def save_results(documents, global_vector, output_file_path):
    with open(output_file_path, 'w') as f:
        for word in global_vector:
            f.write(f"@attribute {word}\n")
        f.write("@data\n")

        for freq_vector, topics in documents:
            vector_str = " ".join([f"{global_vector[word]}:{freq}" for word, freq in freq_vector.items()])
            topics_str = " ".join(topics)
            f.write(f"{vector_str} # {topics_str}\n")
