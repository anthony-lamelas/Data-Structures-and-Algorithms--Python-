def reverse_digits(value):
    reverse = 0
    while value > 0:
        temp = value % 10
        value //= 10
        reverse = reverse*10 + temp

    return reverse

print(reverse_digits(123))