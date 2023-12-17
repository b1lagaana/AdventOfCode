import re

file_data = open("data.txt", "r")
file_data_02 = open("data.txt", "r")
file_data_example_00 = open("example_00.txt", "r")

def day03_task02(data):
    sumnb = 0
    matrix = []
    counter = 0
    nb_matrix = []
    help_nb_matrix = []
    rev_found_numbers_help = []

    for d in data:
        matrix.append((' '.join(d).split("\n")[0]).split(" "))
        counter = counter + 1

    for y in range(counter):
        for x in range(len(matrix[y])):
            if matrix[y][x].isdigit() or matrix[y][x] == "*":
                help_nb_matrix.append(matrix[y][x])
            else:
                help_nb_matrix.append(".")


        nb_matrix.append(help_nb_matrix)
        help_nb_matrix = []

    for y in range(counter):
        for x in range(len(nb_matrix[y])):
            if nb_matrix[y][x] == "*":
                for nb_y in range(y-1, y+2, 1):
                    for nb_x in range(x-1, x+2, 1):
                        if -1 < nb_y < counter:
                            if -1 < nb_x < len(nb_matrix[y]):
                                if nb_matrix[nb_y][nb_x].isdigit():
                                    print(nb_matrix[nb_y][nb_x])
                                    for find in range(nb_x, 0, -1):
                                        if nb_matrix[nb_y][find].isdigit():
                                            rev_found_numbers_help.append(nb_matrix[nb_y][nb_x-find])
                                        else:
                                            break
                                    for newfind in range(nb_x, len(nb_matrix[nb_y]), 1):
                                        if nb_matrix[nb_y][newfind].isdigit():
                                            rev_found_numbers_help.append(nb_matrix[nb_y][newfind])
                                        else:
                                            break
                                    rev_found_numbers_help.append(".")
                                    break

                numbers_find = re.findall(('[0-9]*'), ''.join(rev_found_numbers_help))
                count_nf = 0
                help_multi = 0
                for nf in numbers_find:
                    if nf.isdigit():
                        count_nf = count_nf + 1
                        if count_nf == 1:
                            help_multi = int(nf)
                        elif count_nf == 2:
                            help_multi = help_multi * int(nf)
                            sumnb = sumnb + help_multi
                            count_nf = 0
                print("------")
                rev_found_numbers_help = []

    print("The solution for Day 3 Task 2 is: ", sumnb)




#day03_task02(file_data)
day03_task02(file_data_example_00)
#533775
# 529166
# 113024971 -> too high