def foo(my_list):
    return my_list[len(my_list) - 1]


def banana(your_list):
    return your_list[1:]


def banana2(your_list):
    return your_list[-4:-1]


def last_three(my_list):
    return my_list[-3:]


if __name__ == "__main__":

    beth_list = ["a", 2, "c", 4, 5, 6, 7, "beth", "ghayoung"]
    beth_list = list(range(10))

    print(beth_list)
    print(last_three(beth_list))

    print(beth_list[len(beth_list) - 1])
    print(beth_list[len(beth_list) - 3])

    print(beth_list[-1])
    print(beth_list[-3:-1])
    print(beth_list[4:6])

    print(beth_list[-5:2])

    beth_list = ["a", 2, "c"]
    print(banana(beth_list))
    print(banana2(beth_list))
