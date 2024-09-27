from sys import stdin

next_case = stdin.readline().strip().split()
while next_case != ["0", "0"]:
    setJack = set()
    setJill = set()
    incommon = 0
    for _ in range(int(next_case[0])):
        setJack.add(int(stdin.readline().strip()))
    for _ in range(int(next_case[1])):
        setJill.add(int(stdin.readline().strip()))
    print(len(setJack.intersection(setJill)))
    next_case = stdin.readline().strip().split()
