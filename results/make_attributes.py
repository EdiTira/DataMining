def make_attributes(global_vector_with_gains, file):
    for word, gain in global_vector_with_gains.items():
        file.write(f"@attribute {word}, {gain}\n")

