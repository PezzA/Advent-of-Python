data = open("day1input.txt").read()


def getFloor(data, stopOnBasement):
    floor = 0
    for index, char in enumerate(data):
        floor += 1 if char == "(" else -1

        if floor == -1 and stopOnBasement:
            return index + 1
    return floor


print(f"Part One: {getFloor(data, False)}")
print(f"Part Two: {getFloor(data, True)}")
