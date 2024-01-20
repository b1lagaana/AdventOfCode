import re

file_data = open("data.txt", "r")
file_data_02 = open("data.txt", "r")
file_data_example_00 = open("example_00.txt", "r")


def day04_task01(data):
    winning_numbers = []
    card_numbers = []
    count_lines = 0
    suma = 0
    scratchcards = []

    for line in data.readlines():
        winning_numbers.append((line.split(":")[1]).split("|")[0])
        card_numbers.append((line.split(":")[1]).split("|")[1])
        count_lines = count_lines + 1
        scratchcards.append(0)

    for nl in range(count_lines):
        count_wins = 0
        wn_len = len(winning_numbers[nl].split())
        cn_len = len(card_numbers[nl].split())
        for w in range(wn_len):
            for c in range(cn_len):
                if winning_numbers[nl].split()[w] == card_numbers[nl].split()[c]:
                    if count_wins == 0:
                        count_wins = count_wins + 1
                    else:
                        count_wins = count_wins * 2
                    scratchcards[nl] = scratchcards[nl] + 1

        suma = suma + count_wins

    print("The result of Task 01 on Day 04 is:", suma)
    day04_task02(scratchcards)


def day04_task02(scratchcards):
    total_scratchcards = []
    sum_scratchcards = 0

    index_nb = len(scratchcards)
    for i in range(index_nb):
        total_scratchcards.append(1)

    for i in range(index_nb):
        run_lines = scratchcards[i]
        for cards in range(total_scratchcards[i]):
            for j in range(1,run_lines+1):
                total_scratchcards[j+i] = total_scratchcards[j+i] + 1

    for s in range(index_nb):
        sum_scratchcards = sum_scratchcards + total_scratchcards[s]

    print("The result of Task 01 on Day 04 is:", sum_scratchcards)
    pass



day04_task01(file_data)
#13