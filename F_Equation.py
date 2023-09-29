def sum_of_even_powers_of_x(x, n):
    """Returns the sum of the even powers of x from x0 to xn.

    Args:
      x: The base number.
      n: The upper bound (inclusive).

    Returns:
      The sum of the even powers of x from x0 to xn.
    """

    sum = 0
    for i in range(0, n + 1, 2):
        sum += x ** i

    return sum


def main():
    x, n = map(int, input().split())
    sum_of_even_powers = sum_of_even_powers_of_x(x, n)
    print(sum_of_even_powers)


if __name__ == '__main__':
    main()
