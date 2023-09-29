from collections import Counter

n = int(input())
sequence = list(map(int, input().split()))

counter = Counter(sequence)


removals = 0
for num, count in counter.items():
    if num < count:
        removals += count - num
    elif num > count:
        removals += count

print(removals)
