from results import make_attributes, make_data


def save_results(documents, global_vector, output_file_path):
    with open(output_file_path, 'w') as file:
        make_attributes(global_vector, file)

        file.write("@data\n")

        make_data(documents, global_vector, file)
