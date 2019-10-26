

def foo(my_list):
    return my_list[len(my_list) - 1]


def banana(your_list):
    return your_list[1:]


def banana2(your_list):
    return your_list[-4:-1]


if __name__ == "__main__":

    beth = ['a', 2, 'c', 4, 5, 6, 7]
    # beth = ['a', 2, 'c']

    # print(banana(beth))
    print(banana2(beth))
