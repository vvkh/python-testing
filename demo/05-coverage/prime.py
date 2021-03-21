def is_prime(number):
    for divider in range(2, number):
        if number % divider == 0:
            return False
    return True