file_data = open("data.txt", "r")
file_data_02 = open("data.txt", "r")
file_data_example_00 = open("example_00.txt", "r")

# Task one data
max_numbers_one = ["12 red", "13 green", "14 blue"]

# Task two data
max_numbers_two = []

# task 1
def day02_task01(max_number, numbers):
    sum = 0

    for line in numbers:
        game_id = (line.split(":").__getitem__(0)).split()[1]
        games = (line.split(":").__getitem__(1)).split(";")

        value=check_game(game_id, games, max_number)
        sum = sum + int(value)

    print("The result for task 01 on day 02 is:", sum)



# task 2
def day02_task02(numbers):
    sum = 0

    for line in numbers:
        game_id = (line.split(":").__getitem__(0)).split()[1]
        games = (line.split(":").__getitem__(1)).split(";")

        colours = []
        colour_a_max_nb = []

        for g in games:
            multiply_value = 1
            len_g = len(g.split(","))
            for gc in range(len_g):
                gc_number = g.split(",")[gc].split()[0]
                gc_colour = g.split(",")[gc].split()[1]

                if gc_colour not in colours:
                    colour_a_max_nb.append(gc_colour+" "+gc_number)
                    colours.append(gc_colour)
                else:
                    col_len = len(colour_a_max_nb)
                    for i in range(col_len):
                        if gc_colour in colour_a_max_nb[i]:
                            if int(gc_number) > int(colour_a_max_nb[i].split()[1]):
                                new_value = gc_colour+" "+gc_number
                                colour_a_max_nb[i] = new_value
        len_col_a_max_nb = len(colour_a_max_nb)
        for i in range(len_col_a_max_nb):
            multiply_value = multiply_value * int(colour_a_max_nb[i].split()[1])

        sum = sum + multiply_value
    print("The result for Task 02 on day 02 is:", sum)


def check_game(game_id, games, max_number):
    remove_game_id = False
    len_max = len(max_number)
    max_nb = [max.split().__getitem__(0) for max in max_number]
    max_colour = [max.split().__getitem__(1) for max in max_number]

    for g in games:
        len_g = len(g.split(","))
        for gc in range(len_g):
            gc_number = g.split(",")[gc].split()[0]
            gc_colour = g.split(",")[gc].split()[1]

            for cc in range(len_max):
                if gc_colour == max_colour[cc]:
                    if int(max_nb[cc]) < int(gc_number):
                        remove_game_id = True
                        break
    if not remove_game_id:
        return game_id
    else:
        return 0






day02_task01(max_numbers_one, file_data)
day02_task02(file_data_02)
# read the data
# format data:

# Game-ID: count number of lines
# Game-Record ['3 blue','4 red','1 red', '2 green', '6 blue', '2 green']
# check against each item if color matches and only record highest number of draws:
## 12 red, 13 green, 14 blue -> max numbers of colors
# 3 blue -> not red; not green; 3 blue < 14 blue? -> No: next; Yes, check next in Game-Record; if record is finished add game ID to count
#