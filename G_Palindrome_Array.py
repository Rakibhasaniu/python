# Read input
N = int(input())
A = list(map(int, input().split()))


def is_palindrome(arr):

    reversed_str = arr[::-1]

    if (arr == reversed_str):
        return "YES"
    else:
        return "NO"


result = is_palindrome(A)

print(result)
