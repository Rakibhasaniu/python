n = int(input())
num = list(map(int, input().split()))

maximum = max(num)
minimum = min(num)
max_index = num.index(maximum)
min_index = num.index(minimum)
num[max_index], num[min_index] = num[min_index], num[max_index]
print(*num)
