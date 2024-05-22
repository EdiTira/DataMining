def make_attributes(global_vector, file):
    for word in global_vector:
        file.write(f"@attribute {word}\n")

