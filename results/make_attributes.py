from entropy import make_total_occurrences
from entropy import make_entropy


def make_attributes(global_vector, file):
    total_occurrences = make_total_occurrences(global_vector)

    for word in global_vector:
        entropy = make_entropy(global_vector[word], total_occurrences)
        file.write(f"@attribute {word}, {entropy}\n")

