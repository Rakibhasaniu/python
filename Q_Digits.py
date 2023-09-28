
def reverse_digit(num):
    digit = str(num)
    print(" ".join(digit[::-1]))


test_case = int(input())
for _ in range(test_case):
    n = int(input())
    reverse_digit(n)
