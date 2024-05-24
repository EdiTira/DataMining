from results import make_attributes, make_data


def save_results(documents, global_vector_with_gains, output_file_path):
    with open(output_file_path, 'w') as file:
        make_attributes(global_vector_with_gains, file)

        file.write("@data\n")

        make_data(documents, file)
