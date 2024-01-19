file_data = open("data.txt", "r")
file_data_02 = open("data.txt", "r")
file_data_example_00 = open("example_00.txt", "r")

import re
# Task number one
runtime = []
distance = []
# Task number two


def day06_task01(data):

    for i in data.readlines():
        if i.split(":")[0] == "Time":
            for i in ((((i.split(":")[1]).split("\n")))[0].split(" ")):
                if i.isdigit():
                    runtime.append(i)
        elif i.split(":")[0] == "Distance":
            for i in ((((i.split(":")[1]).split("\n")))[0].split(" ")):
                if i.isdigit():
                    distance.append(i)

    for t in range(len(runtime)):
        run_distance = 0
        for d in range(int(runtime[t])):
            current_time = d * (int(runtime[t])-d)

            if int(distance[t]) < int(current_time):
                run_distance = run_distance + 1

        try:
            number_ways
        except NameError:
            number_ways = run_distance
        else:
            number_ways = int(number_ways)* int(run_distance)


    sum = number_ways
    print("The result of Task 01 on Day 06 is:", sum)


def day06_task02(data):
    runtime = []
    distance = []

    for i in data.readlines():
        if i.split(":")[0] == "Time":
            runtime.append(int(''.join(re.findall(('[0-9]*'), i))))
        if i.split(":")[0] == "Distance":
            distance.append(int(''.join(re.findall(('[0-9]*'), i))))

    for t in range(len(runtime)):
        run_distance = 0
        for d in range(int(runtime[t])):
            current_time = d * (int(runtime[t])-d)

            if int(distance[t]) < int(current_time):
                run_distance = run_distance + 1
        try:
            number_ways
        except NameError:
            number_ways = run_distance
        else:
            number_ways = int(number_ways)* int(run_distance)

    sum = number_ways
    print("The result of Task 02 on Day 06 is:", sum)

day06_task01(file_data)
day06_task02(file_data_02)