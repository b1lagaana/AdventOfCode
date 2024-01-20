import re

coordinates = []
counter = 0
row_counter = 0
run_counter = 0

# function to get FIRST start coordinates
def get_first_starts(coordinates, next_start):
    first_start = []
    for y in range(len(coordinates)):
        if coordinates[y][0][0][2] == next_start:
            first_start.append(coordinates[y])
    return first_start

# function to get next start coordinates
def get_new_start(coordinates, target, next_start):
    for y in range(len(coordinates)):
        if coordinates[y][0][0] == next_start:
            new_next_start = coordinates[y]
            break
    return new_next_start

# get map of coordinates
for i in (open("data.txt", "r").read().splitlines()):
    tuple_data = []
    if counter == 0:
        instructionset = i
        counter += 1
    else:
        if i:
            start = i.split(" = ")[0]
            for cor in re.split('[^0-9a-zA-Z]', i.split(" = ")[1]):
                if cor:
                    tuple_data.append(cor)
                    row_counter += 1

            coordinates.append([[start],[tuple_data[0],tuple_data[1]]])

# run through instructionset
instruction = 0

first_start = "A"

starting_points = (get_first_starts(coordinates, first_start))
#print(starting_points)

while instruction < len(instructionset):
    new_starting_points = []
    if instructionset[instruction] == "L":
        target = 0
    elif instructionset[instruction] == "R":
        target = 1

    attheend = True
    for start, coord in starting_points:
        found_point = get_new_start(coordinates, target, coord[target])
        if found_point[0][0][2] != "Z":
            attheend = False
        elif found_point[0][0][2] == "Z":
            print("Round: ", run_counter, ": ", found_point[0][0])
        new_starting_points.append(found_point)



    starting_points = []
    starting_points = new_starting_points

#    for y in range(len(coordinates)):
#        if coordinates[y][0][0] == next_start:
#            next_start = coordinates[y][1][target]
#            break
    if attheend:
        instruction = len(instructionset)
    elif instruction == len(instructionset)-1:
        instruction = 0
    else:
        instruction += 1
    run_counter += 1

    if run_counter == 66409:
        print(starting_points)
        break
print(run_counter)



