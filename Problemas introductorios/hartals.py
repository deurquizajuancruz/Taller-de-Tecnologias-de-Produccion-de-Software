from sys import stdin


def hartals(days, hartal_parameter):
    daysHartals = [False] * (days + 1)
    for i in hartal_parameter:
        numberDays = 1
        for j in range(1, days + 1):
            if numberDays < 6 and j % i == 0:
                daysHartals[j] = True
            if numberDays == 7:
                numberDays = 1
            else:
                numberDays += 1
    print(sum(daysHartals[2:]))


cases = int(stdin.readline())
for _ in range(cases):
    days = int(stdin.readline())
    parties = int(stdin.readline())
    array = []
    for _ in range(parties):
        array.append(int(stdin.readline()))
    hartals(days, array)
