
n = int(input())
num = list(map(int, input().split()))

flag = True
count = 0

while flag:
    for i in range(n):
        if num[i] % 2 != 0:
            flag = False
            break
    if flag:
        for i in range(n):
            num[i] //= 2
        count += 1

print(count)
