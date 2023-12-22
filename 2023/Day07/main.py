from collections import Counter

play = []
counted = []

for i in (open("example_00.txt", "r").read().splitlines()):
    play.append([i.split(" ")[0], i.split(" ")[1]])

#play[0].insert(2, 0)
for hand, bid in play:
    values = Counter(hand).items()
    try:
        round_count
    except NameError:
        round_count = 0
    else:
        round_count += 1
    for val, num_val in values:
        if num_val == 5:
            play[round_count].append(7)
        if num_val == 4:
            card_type = 6
            if len(play[round_count]) == 3:
                if play[round_count][2] < card_type:
                    play[round_count].pop(2)
                    play[round_count].append(card_type)
            else:
                play[round_count].append(card_type)
        if num_val == 3:
            card_type = 4
            if len(play[round_count]) == 3:
                if play[round_count][2] == 2:
                    play[round_count].pop(2)
                    play[round_count].append(5)
                elif play[round_count][2] < card_type and not play[round_count][2] == 2:
                    play[round_count].pop(2)
                    play[round_count].append(card_type)
            else:
                play[round_count].append(card_type)
        if num_val == 2:
            card_type = 2
            if len(play[round_count]) == 3:
                if play[round_count][2] == 4:
                    play[round_count].pop(2)
                    play[round_count].append(5)
                elif play[round_count][2] == card_type:
                    play[round_count].pop(2)
                    play[round_count].append(3)
                elif play[round_count][2] < card_type:
                    play[round_count].pop(2)
                    play[round_count].append(card_type)
            else:
                play[round_count].append(card_type)
        if num_val == 1:
            card_type = 1
            if len(play[round_count]) == 3:
                if play[round_count][2] < card_type:
                    continue
            else:
                play[round_count].append(card_type)
    print("----------")

print(play)


# check out max number of one card
# check out what type hand has:
# #five of cards,
# four of kind,
# full house,
# three of kind,
# two pair,
# one pair,
# high card:
# check out max value of cards

# get rank of hand, multiply rank with bid for hand and add all set of hands winnings together

