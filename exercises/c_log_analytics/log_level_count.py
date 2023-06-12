def log_analysis(input_file):
    with open(input_file, 'r') as file:
        log_entries = file.readlines()

    # TODO: MapReduce

    # TODO: Print word counts


if __name__ == '__main__':
    log_file = "../resources/logs.txt"
    log_analysis(log_file)
