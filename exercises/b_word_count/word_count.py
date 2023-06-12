import re


# TODO Map function: split text into words and emit key-value pairs
def map_function(text):
    return None


# TODO Reduce function: aggregate the counts for each word
def reduce_function(counts, word):
    return None


def word_count(path):
    with open(path, 'r') as file:
        lines = file.readlines()

    # TODO: MapReduce

    # TODO: Print word counts


if __name__ == '__main__':
    file_path = "../resources/text.txt"
    word_count(file_path)
