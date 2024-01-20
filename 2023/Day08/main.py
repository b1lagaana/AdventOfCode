import re

coordinates = []
counter = 0
row_counter = 0
run_counter = 0

# get map of coordinates
for i in (open("data.txt", "r").read().splitlines()):
    tuple_data = []
    if counter == 0:
        instructionset = i
        counter += 1
    else:
        if i:
            start = i.split(" = ")[0]
            for cor in re.split('[^a-zA-Z]', i.split(" = ")[1]):
                if cor:
                    tuple_data.append(cor)
                    row_counter += 1

            coordinates.append([[start],[tuple_data[0],tuple_data[1]]])
# print("start:", coordinates[0][0][0], "left_point:", coordinates[0][1][0], "right point:", coordinates[0][1][1])

# run through instructionset
instruction = 0

while instruction < len(instructionset):

    try:
        next_start
    except NameError:
        next_start = "AAA"

    if instructionset[instruction] == "L":
        target = 0
    elif instructionset[instruction] == "R":
        target = 1

    for y in range(len(coordinates)):
        if coordinates[y][0][0] == next_start:
            next_start = coordinates[y][1][target]
            break
    if next_start == "ZZZ":
        instruction = len(instructionset)
    elif instruction == len(instructionset)-1:
        instruction = 0
    else:
        instruction += 1
    run_counter += 1

print(run_counter)



