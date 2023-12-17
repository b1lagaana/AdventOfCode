play = []

for i in (open("example_00.txt", "r").read().splitlines()):
    play.append((i.split(" ")[0], i.split(" ")[1]))

# get rank of hand, multiply rank with bid for hand and add all set of hands winnings together

