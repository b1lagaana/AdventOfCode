file_data = open("data.txt", "r")
file_data_02 = open("data.txt", "r")
file_data_example_01 = open("example_01.txt", "r")
file_data_example_02 = open("example_02.txt", "r")


# Task number one
## get different lists
list_data = []

def get_lists(data):
    list_seed_extended = []

    for i in data.readlines():
        list = ''.join(i.split("\n"))
        list_data.append(list)

    for r in range(len(list_data)):
        if "seeds:" in list_data[r]:
            list_seed = list_data[r].split(":")[1].split()
        elif "seed-to-soil" in list_data[r]:
            list_map_ss = assign_values(list_data, r)
        elif "soil-to-fertilizer" in list_data[r]:
            list_map_sf = assign_values(list_data, r)
        elif "fertilizer-to-water" in list_data[r]:
            list_map_fw = assign_values(list_data, r)
        elif "water-to-light" in list_data[r]:
            list_map_wl = assign_values(list_data, r)
        elif "light-to-temperature" in list_data[r]:
            list_map_lt = assign_values(list_data, r)
        elif "temperature-to-humidity" in list_data[r]:
            list_map_th = assign_values(list_data, r)
        elif "humidity-to-location" in list_data[r]:
            list_map_hl = assign_values(list_data, r)

    for i in range(0, len(list_seed), 2):
        start = int(list_seed[i])
        duration = int(list_seed[i]) + int(list_seed[i + 1])
        for e in range(start, duration):
            list_seed_extended.append(e)
            if e == 100:
                break
            print(e)

        print("----------------")

    print(list_seed_extended)

    first_return = calculate(list_seed, list_map_ss, list_map_sf, list_map_fw, list_map_wl, list_map_lt, list_map_th, list_map_hl)
    day05_task01(first_return)
    #second_return = calculate(list_seed_extended, list_map_ss, list_map_sf, list_map_fw, list_map_wl, list_map_lt, list_map_th, list_map_hl)
    #day05_task02(second_return)

def assign_values(list_data, r):
    list_map = []
    for m in range(len(list_data)-r):
        if len(list_data) == r+m+1:
            break
        if len(list_data[r+m+1]) != 0:
            list_map.append(list_data[r+m+1])
        else:
            break
    return list_map
def calculate(list_seed, list_map_ss, list_map_sf, list_map_fw, list_map_wl, list_map_lt, list_map_th, list_map_hl):
    for s in range(len(list_seed)):
        temp = calulate_location(list_seed[s], list_map_ss)
        temp = calulate_location(temp, list_map_sf)
        temp = calulate_location(temp, list_map_fw)
        temp = calulate_location(temp, list_map_wl)
        temp = calulate_location(temp, list_map_lt)
        temp = calulate_location(temp, list_map_th)
        temp = calulate_location(temp, list_map_hl)

        try:
            lowest_location_nb
        except NameError:
            lowest_location_nb = temp
        else:
            if temp < lowest_location_nb:
                lowest_location_nb = temp
    return lowest_location_nb

def calulate_location(s, list_map):
    mapped = 0

    for dr_sr_rl in range(len(list_map)):
        dest_range = list_map[dr_sr_rl].split()[0]
        source_range = list_map[dr_sr_rl].split()[1]
        range_length = list_map[dr_sr_rl].split()[2]

        if int(source_range) <= int(s) <= int(source_range)+int(range_length):
            mapped = (int(s)+(int(dest_range)-int(source_range)))
            break

    if mapped == 0:
        mapped = s

    return mapped