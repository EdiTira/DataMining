from enums import DataSetPath

_choice = {
    1: DataSetPath.TRAINING_PATH.value,
    2: DataSetPath.TESTING_PATH.value,
    3: DataSetPath.REUTERS_7083_PATH.value,
}


def get_data_set_path(user_choice):
    try:
        return _choice[user_choice]
    except KeyError:
        raise ValueError("Invalid user choice. Please select a valid option.")
