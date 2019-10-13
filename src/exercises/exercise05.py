
def is_prime(number):
    prime = True

    for d in range(2, number):
        if number % d == 0:
            prime = False
            break

    return prime


N = 1000

for n in range(2, N):
    if is_prime(n):
        print(n)
