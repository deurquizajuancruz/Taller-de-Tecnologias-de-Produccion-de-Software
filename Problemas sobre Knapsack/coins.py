from sys import stdin, stdout


def coins_max(coins, half) -> int:
    array = [0] * (half + 1)
    for coin in coins:
        for j in range(half, coin - 1, -1):
            array[j] = max(array[j], array[j - coin] + coin)
            if array[j] == half:
                return half

    return array[half]


data = stdin.read().splitlines()
cases = int(data[0])
index = 1
results = []

for _ in range(cases):
    number_coins = int(data[index])
    coins = list(map(int, data[index + 1].split()))
    total = sum(coins)
    half = total // 2
    results.append(str(total - 2 * coins_max(coins, half)))
    index += 2

stdout.write("\n".join(results) + "\n")
