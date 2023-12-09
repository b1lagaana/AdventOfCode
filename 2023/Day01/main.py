# Advent of Code Day 1

import re

file_data = open("data.txt", "r")
file_data_02 = open("data.txt", "r")
file_data_example_01 = open("example_01.txt", "r")
file_data_example_02 = open("example_02.txt", "r")
file_data_example_02_ext = open("example_02_extended.txt", "r")

def day01_task01(data):
    sum = 0

    for line in data.readlines():
        digit = ''.join(re.findall(('[0-9]*'), line))
        print(digit)
        count = len(digit)
        number = (int(digit.__getitem__(0)) * 10) + int(digit.__getitem__(count - 1))
        sum = sum + number

    print("Results for task number 1:", sum)

def day01_task02(data):
    sum = 0
    help_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0',
        'oneight': '18',
        'threeight': '38',
        'fiveight': '58',
        'sevenine': '79',
        'eightwo': '82',
        'eighthree': '83',
        'nineight': '98'
    }

    for line in data.readlines():
        digit = ' '.join(re.findall(('[0-9]|oneight|threeight|fiveight|sevenine|eightwo|eighthree|nineight|one|two|three|four|five|six|seven|eight|nine]*'), line))
        strg_number_line = ""

        for ele in digit.split():
            if ele in help_dict:
                strg_number = ''.join(help_dict[ele])
            else:
                strg_number = ''.join(ele)
            strg_number_line = strg_number_line + strg_number

        count = len(strg_number_line)
        strg_digit = (int(strg_number_line.__getitem__(0)) * 10) + (int(strg_number_line.__getitem__(count-1)))
        sum = sum + strg_digit

    print("Results for task number 2:", sum)


day01_task01(file_data)

day01_task02(file_data_02)
