def creating_solution_matrix(width, length):
    solution_matrix = [[0 for _ in range(width)] for _ in range(length)]

    for i in range(1, length - 1):
        solution_matrix[i][width - 1] = None

    solution_matrix[0][width - 1] = 1
    solution_matrix[length - 1][width - 1] = 1

    return solution_matrix


def find_successful_ways(letter_tile, column, width, length,
                         solution_matrix, input_matrix):
    ways = None

    if solution_matrix[column][letter_tile + 1] is not None:
        ways = solution_matrix[column][letter_tile + 1]

    for current_column in range(0, length):
        for current_tile in range(letter_tile + 1, width):

            if input_matrix[column][letter_tile] == input_matrix[current_column][current_tile]:
                if current_tile == letter_tile + 1 and current_column == column:
                    continue

                if solution_matrix[current_column][current_tile] is not None:
                    if ways is None:
                        ways = 0
                    ways += solution_matrix[current_column][current_tile]

    solution_matrix[column][letter_tile] = ways


def get_paths_number(filename):
    width, length, input_matrix = get_info(filename)

    solution_matrix = creating_solution_matrix(width, length)
    for current_plate in range(width - 2, -1, -1):
        for current_column in range(length - 1, -1, -1):
            find_successful_ways(current_plate, current_column,
                                 width, length, solution_matrix, input_matrix)

    solution_in_line = 0
    for column in range(length):
        if solution_matrix[column][0] is not None:
            solution_in_line += solution_matrix[column][0]

    return solution_in_line


def get_info(filename):
    with open(filename, 'r') as file:
        width, length = (list(map(int, file.readline().split())))
        input_matrix = []
        for line in file:
            input_matrix.append(line.strip())
    return width, length, input_matrix



