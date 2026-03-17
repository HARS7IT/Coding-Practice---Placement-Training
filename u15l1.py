def butterfly(n):
    pattern = []

    # Upper Half
    for i in range(1, n + 1):
        line = (
            "*" * i +
            " " * (2 * (n - i)) +
            "*" * i
        )
        pattern.append(line)

    # Lower Half
    for i in range(n, 0, -1):
        line = (
            "*" * i +
            " " * (2 * (n - i)) +
            "*" * i
        )
        pattern.append(line)

    return "\n".join(pattern)
output = butterfly(5)
print(output)

