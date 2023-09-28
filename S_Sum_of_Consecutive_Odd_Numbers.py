# Function to calculate the sum of odd numbers between X and Y (excluding X and Y)
def sum_odd_numbers_between(X, Y):
    total_sum = 0
    for num in range(X + 1, Y):
        if num % 2 != 0:
            total_sum += num
    return total_sum


# Input number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Input X and Y for the current test case
    X, Y = input().split()
    X = int(X)
    Y = int(Y)

    # Calculate and print the sum of odd numbers between X and Y
    result = sum_odd_numbers_between(X, Y)
    print(result)
