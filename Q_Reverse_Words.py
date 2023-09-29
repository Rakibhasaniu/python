s = input()
words = s.split()

for word in words:
    reversed = word[::-1]
    print(reversed, end=' ')
print()
