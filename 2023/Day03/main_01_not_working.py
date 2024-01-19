import re

file_data = open("data.txt", "r")
file_data_02 = open("data.txt", "r")
file_data_example_00 = open("example_00.txt", "r")

def day03_task01(data):
    sum = 0
    matrix = []
    nb_matrix = []

    for d in data:
        matrix.append((' '.join(d).split("\n")[0]).split(" "))

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
        for x in range(len(matrix[y])):
            try:
                wr_vals
            except NameError:
                wr_vals = False
            else:
                pass

            if wr_vals and x <= pos-1:
                nb_matrix.append(matrix[y][x])
            elif matrix[y][x].isdigit():
                nb_range = trailing_numbers(matrix, y, x)
                pos = nb_range + x
                wr_vals = check_val(matrix, y, x, pos)
                if wr_vals:
                    nb_matrix.append(matrix[y][x])
                else:
                    nb_matrix.append(".")
            else:
                wr_vals = False
                nb_matrix.append(".")

    numbers_find = re.findall(('[0-9]*'), ''.join(nb_matrix))


   # print(numbers_find)
    for n in numbers_find:

        if n.isdigit():
            sum = sum + int(n)

    print("The answer to Day 03 Task 01 is: ", sum)



def trailing_numbers(matrix, y, x):
    counter = 1
    continue_check = True

    while(continue_check):
        try:
            matrix[y][x+counter]
        except IndexError:
            continue_check = False
        else:
            if matrix[y][x+counter].isdigit():
                counter = counter + 1
            else:
                continue_check = False
    return counter

def check_val(matrix, y, x, lst):

    count = False
    for r in range(x, lst):
        try:
            matrix[y-1][r-1]
        except IndexError:
            pass
        else:
            if matrix[y-1][r-1].isprintable() and matrix[y-1][r-1] != "" and not (matrix[y-1][r-1].isdigit() or matrix[y-1][r-1] == "."):
                count = True

        try:
            matrix[y-1][r]
        except IndexError:
            pass
        else:
            if matrix[y-1][r].isprintable() and matrix[y-1][r] != "" and not (matrix[y-1][r].isdigit() or matrix[y-1][r] == "."):
                count = True

        try:
            matrix[y-1][r+1]
        except IndexError:
            pass
        else:
            if matrix[y-1][r+1].isprintable() and matrix[y-1][r+1] != ""  and not (matrix[y-1][r+1].isdigit() or matrix[y-1][r+1] == "."):
                count = True

        try:
            matrix[y][r-1]
        except IndexError:
            pass
        else:
            if matrix[y][r-1].isprintable() and matrix[y][r-1] != ""  and not (matrix[y][r-1].isdigit() or matrix[y][r-1] == "."):
                count = True

        try:
            matrix[y][r+1]
        except IndexError:
            pass
        else:
            if matrix[y][r+1].isprintable() and matrix[y][r+1] != ""  and not (matrix[y][r+1].isdigit() or matrix[y][r+1] == "."):
                count = True

        try:
            matrix[y+1][x-1]
        except IndexError:
            pass
        else:
            if matrix[y+1][r-1].isprintable() and matrix[y+1][r-1] != ""  and not (matrix[y+1][r-1].isdigit() or matrix[y+1][r-1] == "."):
                count = True

        try:
            matrix[y+1][r]
        except IndexError:
            pass
        else:
            if matrix[y+1][r].isprintable() and matrix[y+1][r] != ""  and not (matrix[y+1][r].isdigit() or matrix[y+1][r] == "."):
                count = True

        try:
            matrix[y+1][r+1]
        except IndexError:
            pass
        else:
            if matrix[y+1][r+1].isprintable() and matrix[y+1][r+1] != ""  and not (matrix[y+1][r+1].isdigit() or matrix[y+1][r+1] == "."):
                count = True
    return count


def day03_task02(matrix, nb_matrix):
    pass


day03_task01(file_data)
#day03_task01(file_data_example_00)
#533775
# 529166