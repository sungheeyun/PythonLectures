"""
Print out all divisors of a given number
"""

number = int(input("number? "))

print(1)
for divisor in range(2, number):
    if number % divisor == 0:
        print(divisor)

print(number)
