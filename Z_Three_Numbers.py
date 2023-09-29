# Function to count the number of different values of X, Y, and Z
def count_values(K, S):
    count = 0

    for X in range(K + 1):
        for Y in range(K + 1):
            Z = S - X - Y
            if 0 <= Z <= K:
                count += 1

    return count


# Input K and S
K, S = map(int, input().split())

# Count and print the number of different values of X, Y, and Z
result = count_values(K, S)
print(result)
