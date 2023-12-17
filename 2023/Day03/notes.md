
        try:
            counter
        except NameError:
            counter = 1
        else:
            counter = counter + 1

    for y in range(counter):
        try:
            max_length
        except NameError:
            max_length = len(matrix[y])

        if max_length > len(matrix[y]):
            matrix[y].append("")
        else:
            max_length = len(matrix[y])

    for y in range(len(matrix)):
        nb_help_matrix = []
        for x in range(len(matrix[y])):
            try:
                wr_vals
            except NameError:
                wr_vals = False
            else:
                pass

            if wr_vals and x <= pos-1:
                nb_help_matrix.append(matrix[y][x])
            elif matrix[y][x].isdigit():
                nb_range = trailing_numbers(matrix, y, x)
                pos = nb_range + x
                wr_vals = check_val(matrix, y, x, pos)
                if wr_vals:
                    nb_help_matrix.append(matrix[y][x])
                else:
                    nb_help_matrix.append(".")
            else:
                wr_vals = False
                nb_help_matrix.append(".")
        nb_matrix.append(nb_help_matrix)

    for row in range(counter):
        for column in range(len(matrix[row])):
            if matrix[row][column] == "*":
                star_matrix.append([row, column])

    count_nb = 0
    for line in star_matrix:
        y = line[0]
        x = line[1]
        for nb_y in range(y-1, y+2, 1):
            if -1 < nb_y < counter:
                for nb_x in range(x-1, x+2, 1):
                    if -1 < nb_x < len(nb_matrix):
                        if nb_matrix[nb_y][nb_x].isdigit():
                            count_nb = count_nb + 1
                            print(count_nb, nb_matrix[nb_y][nb_x])

                if count_nb == 2:
                    counted_star_matrix.append([y, x])
                    count_nb = 0



   # print(numbers_find)
   # find_counter = 0
   # for n in numbers_find:

    #    if n.isdigit():
    #       find_counter = find_counter + 1
    #       if find_counter == 2:
    #          multiply_numbers = multiply_numbers * n
    #          find_counter = 0
    #          sum = sum + multiply_numbers
    #       else:
    #          multiply_numbers = n

    print("The answer to Day 03 Task 02 is: ", sum)


eine Zahl:
[
    [   [0, 0], 
        [0, 0]
    ], 
    [
        [0, 0], 
        [0, 2]
    ]
]