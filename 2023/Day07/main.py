from collections import Counter

play = []
counted = []

for i in (open("data.txt", "r").read().splitlines()):
    play.append([i.split(" ")[0], i.split(" ")[1]])

#play[0].insert(2, 0)
for hand, bid in play:

    justnumbers = []
    for j in range(len(hand)):
        if hand[j] == "A":
            justnumbers.append(14)
        elif hand[j] == "K":
            justnumbers.append(13)
        elif hand[j] == "Q":
            justnumbers.append(12)
        elif hand[j] == "J":
            justnumbers.append(11)
        elif hand[j] == "T":
            justnumbers.append(10)
        else:
            justnumbers.append(int(hand[j]))

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
    play[round_count].append(justnumbers)

type_seven = []
type_six = []
type_five = []
type_four = []
type_three = []
type_two = []
type_one = []

for hand, bid, card_type, numbers_list in play:
    if card_type == 7:
        type_seven.append([numbers_list, hand, bid, card_type])
    elif card_type == 6:
        type_six.append([numbers_list, hand, bid, card_type])
    elif card_type == 5:
        type_five.append([numbers_list, hand, bid, card_type])
    elif card_type == 4:
        type_four.append([numbers_list, hand, bid, card_type])
    elif card_type == 3:
        type_three.append([numbers_list, hand, bid, card_type])
    elif card_type == 2:
        type_two.append([numbers_list, hand, bid, card_type])
    elif card_type == 1:
        type_one.append([numbers_list, hand, bid, card_type])


# sort the card types start with type_one ....type_seven


listofLines =  ['log opened 16-Feb-2010 06:37:56 UTC',
                '06:37:58 Custom parameters are in use',
                'log closed 16-Feb-2010 05:26:47 UTC']
listofTimes = ['06:37:56', '06:37:58', '05:26:47']
sortedIndex = [2,0,1]

# A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2

#[print(listofLines[i]) for i in sortedIndex]
rank = 1
sum = 0
if len(type_one):
  for i in sorted(type_one):
      sum = sum + (float(i[2]) * rank)
      rank += 1
if len(type_two):
  for i in sorted(type_two):
      sum = sum + (float(i[2]) * rank)
      rank += 1
if len(type_three):
  for i in sorted(type_three):
      sum = sum + (float(i[2]) * rank)
      rank += 1
if len(type_four):
  for i in sorted(type_four):
      sum = sum + (float(i[2]) * rank)
      rank += 1
if len(type_five):
  for i in sorted(type_five):
      sum = sum + (float(i[2]) * rank)
      rank += 1
if len(type_six):
  for i in sorted(type_six):
      sum = sum + (float(i[2]) * rank)
      rank += 1
if len(type_seven):
  for i in sorted(type_seven):
      sum = sum + (float(i[2]) * rank)
      rank += 1

print(int(sum))

#print(sorted(type_one))
#print(sorted(type_two))
#print(sorted(type_three))
#print(sorted(type_four))
#print(sorted(type_five))
#print(sorted(type_six))
#print(sorted(type_seven))
#print(type_one.sort(key=str.lower()))
#['KK677','T55J5','33332','32T3K','2AAAA']

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
