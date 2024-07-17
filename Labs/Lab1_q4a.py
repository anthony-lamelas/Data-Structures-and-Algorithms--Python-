def powers_of_two(n):
    for i in range(n):
        yield 2**i


power = powers_of_two(6)
for i in power:
    print(i)

    