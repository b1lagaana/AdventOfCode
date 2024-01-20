
def extrapolate(array):
    if all(x == 0 for x in array):
        return 0

    deltas = [y - x for x,y in zip(array, array[1:])]
    diff = extrapolate(deltas)
    return array[-1] + diff

total = 0

for line in open("data.txt"):
    history_sets = list(map(int, line.split()))

    if history_sets:
        total += extrapolate(history_sets)

print(total)
