from numpy.random import choice
import time


def list_overlap(list1, list2):
    int_list = list()

    for number in list1:
        if number in int_list:
            continue

        if number in list2:
            int_list.append(number)

    return int_list


if __name__ == "__main__":
    # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    n = 1000000
    m = 50000

    a = choice(range(n), m)
    b = choice(range(n), m)

    print(a)
    print(b)

    t0 = time.time()
    print(sorted(list_overlap(a, b)))
    elapsed_time1 = time.time() - t0
    print(f"list_overlap took {elapsed_time1} sec.")

    t0 = time.time()
    print(sorted(list(set(a).intersection(b))))
    elapsed_time2 = time.time() - t0
    print(f"list_overlap took {elapsed_time2} sec.")

    print(f"time ratio = {elapsed_time1/elapsed_time2}")
