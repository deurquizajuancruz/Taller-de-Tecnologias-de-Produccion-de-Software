from sys import stdin

def largest(numbers):
    n = len(numbers)
    lis = [1] * n

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if numbers[i] < numbers[j]:
                lis[i] = max(lis[i], 1 + lis[j])

    return max(lis)

input_data = stdin.read().strip().splitlines()

for i in range(0, len(input_data), 2):
    n = int(input_data[i])
    numbers = list(map(int, input_data[i + 1].split()))
    print(largest(numbers))