from itertools import permutations
from time import time


def find_max_combination(digit_list):
    """
    Find the maximum number that can be obtained by multiplying 3-digit number and 2-digit number
    where the 5 digits in those numbers are chosen from digit_list without replacement.

    :param digit_list:
    :return:
    """
    max_value = 0
    max_sequence = digit_list
    for sequence in permutations(digit_list, 5):
        a = sequence[0] * 100 + sequence[1] * 10 + sequence[2]
        b = sequence[3] * 10 + sequence[4]

        product = a * b
        if product > max_value:
            max_value = product
            max_sequence = sequence

    return max_value, '%d%d%d X %d%d' % max_sequence


if __name__ == "__main__":
    t0 = time()
    print(find_max_combination([9, 7, 5, 4, 3]))
    print('The calculation took %g sec.' % (time() - t0))
