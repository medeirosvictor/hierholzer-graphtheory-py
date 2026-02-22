#!/usr/bin/python


def read_file():

    """Reads input from .txt file and returns graph_size, adj_matrix and adj_list"""
    import glob

    print('Reading input test file inside test/ directory...')
    file_path = glob.glob("test/*.txt")
    file1 = file_path[0]

    adj_matrix = []
    with open(file1, 'r') as test_file:
        graph_size = int(test_file.readline())
        for line in test_file:
            matrix_row = list(map(str, line.split(" ")))
            matrix_row = (map(lambda x: x.strip(), matrix_row))
            adj_matrix.append(matrix_row)
    return graph_size, adj_matrix
