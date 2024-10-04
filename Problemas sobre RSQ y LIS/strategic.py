from sys import stdin
def max_hits(missiles):
    hits = 0
    for i in range(len(missiles)):
        if i == len(missiles):
            hits+=1
            break
        if missiles[i] < missiles[i+1]:
            hits+=1
    return hits

missiles = []
while True:
    missile = stdin.readline()
    if not missile:
        break
    missiles.append(int(missile))

print(max_hits(missiles))