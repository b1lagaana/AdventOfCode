file_data = "data.txt"
file_data_02 = open("data.txt", "r")
file_data_example_01 = "example_00.txt"

from collections import defaultdict

card_list = {"A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"}


fullhouse = False
twopair = False

for line in open(file_data_example_01):
    value = ([line.split('\n')[0].split(' ')[0], line.split('\n')[0].split(' ')[1], ""])
    print(value[0])
    print(value[0].count("A"))
    print(value[0].count("K"))
    print(value[0].count("Q"))
    print(value[0].count("J"))
    print(value[0].count("T"))
    print(value[0].count("9"))
    print(value[0].count("8"))
    print(value[0].count("7"))
    print(value[0].count("6"))
    print(value[0].count("5"))
    print(value[0].count("4"))
    print(value[0].count("3"))
    print(value[0].count("2"))


print("----------------")