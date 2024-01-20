data = open("example_00.txt", "r")

star_list = []
number_list = []
#test_list = ())
start_x = -1
start_y = -1
end_x = -1
end_y = -1
count_number_y = -1
matrix = []
sumnb = 0

list_test = ([[0,1],[2,3]])

for line in data:

    try:
        counter_y
    except NameError:
        counter_y = 0
    else:
        counter_y = counter_y + 1

    matrix.append((' '.join(line).split("\n")[0]).split(" "))

    for i in range(len(line)):
        if line[i] == "*":
            star_list.append([counter_y, i])
            start_x = -1
            start_y = -1
            end_x = -1
            end_y = -1
        elif line[i].isdigit():
            if start_x == -1 and start_y == -1:
                start_y = counter_y
                start_x = i
                end_y = counter_y
                end_x = i
                number_list.append([[start_y, start_x]])
                count_number_y = count_number_y + 1
            else:
                end_y = counter_y
                end_x = i
                number_list[count_number_y].insert(1, [end_y, end_x])
                if len(number_list[count_number_y]) > 2:
                    number_list[count_number_y].pop(2)
        else:
            start_x = -1
            start_y = -1
            end_x = -1
            end_y = -1

for star_row in range(len(star_list)):
    star_y = star_list[star_row][0]
    star_x = star_list[star_row][1]
    found_numbers = 0
    use_number = False
    found_numbers_list = []
    for row in range(len(number_list)):
        for i in range(number_list[row][0][1], number_list[row][1][1]+1):
            number_y = number_list[row][0][0]
            number_x = i
            if number_y-1 <= star_y <= number_y+1:
                if number_x-1 <= star_x <= number_x+1:
                    #print("within range", star_y, number_y, "number at:", number_y, number_x)
                    use_number = True
                    found_numbers = found_numbers + 1
                    found_numbers_list.append([[number_list[row][0][0],number_list[row][0][1]],[number_list[row][1][0],number_list[row][1][1]]])
                    break

            # define var so number can be used, count how many numbers relate to star ()
            # when star_y and star_x is about to change, check if exactly two numbers where found, if not discard
            # if yes multiply the two, set counter to zero and clear list of found numbers
            # add numbers by: set number to zero, start rotating through indexes, multiply set number by 10, add current number
             # check row above, x-1 until x+1
            #print("number index:", number_list[row][0][0], i)

        if use_number:
            if len(found_numbers_list) == 2:
                for line in found_numbers_list:
                    start_y = line[0][0]
                    start_x = line[0][1]
                    end_x = line[1][1] + 1
                    number_multi = 0
                    prev_multi = 1
                    for i in range(start_x, end_x):
                        number_multi = number_multi * 10
                        number_multi = number_multi + int(matrix[start_y][i])
                    print(number_multi)
                    prev_multi = prev_multi * number_multi

                sumnb = sumnb + prev_multi
                found_numbers_list = []
            use_numer = False
        print("-------")

            # check right and left
            # check row below, x-1 until x+1



tuple_list_stars = tuple(star_list)
tuple_list_numbers = tuple(number_list)
previous_y = 0
previous_x = 0



# get indizes of numbers
for number in sorted(tuple_list_numbers):
    try:
        counter
    except NameError:
        counter = 0
    else:
        counter = counter + 1



#print(len(test_list))
#test_list.append([[number_list[0][0],number_list[0][1]]])

#print(len(test_list))
#test_list[0].extend([[number_list[1][0],number_list[1][1]]])
#test_list.append([[number_list[1][0],number_list[1][1]]])
#test_list[1].extend([[number_list[1][0],number_list[1][1]]])
#print(test_list)




find_test = ([1,3],[8,6],[9,6],[8,4])

#for i in sorted(list_test):
#        print(i)

#for j in sorted(find_test):
#        print(j)