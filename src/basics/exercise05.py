def is_prime(number):
    _is_prime = True

    for d in range(2, number):
        if number % d == 0:
            _is_prime = False
            break

    return _is_prime


if __name__ == "__main__":
    N = 1000

    for n in range(2, N):
        if is_prime(n):
            print(n)
