# N = int(input('N? '))
N = 100

for n in range(2, N):
    is_prime = True
    for d in range(2, n):
        if n % d == 0:
            is_prime = False
            break
    if is_prime:
        print(n)
