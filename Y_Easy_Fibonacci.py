# Function to generate Fibonacci numbers using memoization
def generate_fibonacci(N, memo):
    if N <= 1:
        return N
    elif N in memo:
        return memo[N]
    else:
        memo[N] = generate_fibonacci(
            N - 1, memo) + generate_fibonacci(N - 2, memo)
        return memo[N]


# Input N
N = int(input())

# Initialize memoization dictionary to store calculated Fibonacci numbers
memo = {}

# Generate and print the first N Fibonacci numbers
for i in range(N):
    print(generate_fibonacci(i, memo), end=" ")
